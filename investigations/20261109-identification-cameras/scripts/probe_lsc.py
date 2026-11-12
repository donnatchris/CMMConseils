#!/usr/bin/env python3
"""Read-only, bounded LSC cache probes. Never export keys or plaintext payloads."""
import argparse, base64, collections, hashlib, json, math, plistlib, re, zlib
from pathlib import Path
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / 'telephones/recherche-TP-02/extraction-cameras-20261014'
APP = BASE / 'files/AppDomain-com.lscsmartconnection.smart'
parser = argparse.ArgumentParser()
parser.add_argument('--out', required=True)
args = parser.parse_args()
out = Path(args.out)
out.mkdir(parents=True, exist_ok=False, mode=0o700)
sha = lambda d: hashlib.sha256(d).hexdigest()
sources = {}
logs = [json.loads(x) for x in (BASE/'extraction.jsonl').read_text().splitlines()]
expected = {x['relativePath']: x['sha256'] for x in logs
            if x.get('domain') == 'AppDomain-com.lscsmartconnection.smart' and x.get('status') == 'ok'}

def read(p):
    data = p.read_bytes()
    name = str(p.relative_to(APP))
    digest = sha(data)
    if name not in expected or digest != expected[name]:
        raise ValueError('Missing/mismatched extraction hash: ' + name)
    sources[name] = {'bytes': len(data), 'sha256_before': digest, 'extraction_match': True}
    return data

def parse(data):
    for f in (json.loads, plistlib.loads):
        try:
            obj = f(data)
            if isinstance(obj, (dict, list)):
                return obj
        except Exception:
            pass
    return None

seeds = set()
def collect(x):
    if isinstance(x, dict):
        for k, v in x.items():
            collect(k); collect(v)
    elif isinstance(x, list):
        for v in x: collect(v)
    elif isinstance(x, str):
        if 4 <= len(x) <= 512:
            seeds.add(x.encode())
            if re.fullmatch(r'[0-9a-fA-F]+', x) and len(x) % 2 == 0:
                seeds.add(bytes.fromhex(x))
            try:
                v = base64.b64decode(x, validate=True)
                if 4 <= len(v) <= 512: seeds.add(v)
            except Exception: pass
    elif isinstance(x, bytes):
        if 4 <= len(x) <= 512: seeds.add(x)
        obj = parse(x)
        if obj is not None: collect(obj)

prefs = plistlib.loads(read(APP/'Library/Preferences/com.lscsmartconnection.smart.plist'))
collect(prefs)
decoded_resources = []
identity_fields = []
field_re = re.compile(r'^(?:model|modelId|modelName|firmware|firmwareVersion|fwVersion|swVer|swVersion|productId|productKey|devId)$', re.I)
def identities(obj, filename, trail=''):
    if isinstance(obj, dict):
        for k, v in obj.items():
            path = trail + '/' + str(k)
            if field_re.fullmatch(str(k)) and isinstance(v, (str, int, float)):
                # Store field names and value hashes only until device provenance is established.
                identity_fields.append({'source': filename, 'field': str(k), 'value_sha256': sha(str(v).encode())})
            identities(v, filename, path)
    elif isinstance(obj, list):
        for v in obj: identities(v, filename, trail)

for p in sorted(APP.rglob('*')):
    if not p.is_file() or p.stat().st_size > 2_000_000: continue
    rel = str(p.relative_to(APP))
    if not (p.suffix in ('.plist', '.json') or rel.startswith('Documents/mmkv/') or p.name.endswith('_basicinfo')): continue
    data = read(p)
    obj = parse(data)
    encoding = 'json/plist'
    if obj is None:
        try:
            obj = parse(base64.b64decode(data, validate=True)); encoding = 'base64+json/plist'
        except Exception: pass
    if obj is not None:
        # Panel JSONs are translation dictionaries; these do not contain device states.
        translations = isinstance(obj, dict) and bool(set(obj) & {'fr', 'en', 'zh'}) and all(isinstance(v, dict) for v in obj.values())
        decoded_resources.append({'source': rel, 'encoding': encoding, 'translation_dictionary': translations})
        if not translations:
            collect(obj); identities(obj, rel)
    elif rel.startswith('Documents/mmkv/') and not rel.endswith('.crc'):
        for s in re.findall(rb'[A-Za-z0-9_.:@/-]{8,128}', data): seeds.add(s)

keys = set()
for s in seeds:
    if len(s) in (16, 24, 32): keys.add(s)
    keys.add(hashlib.md5(s).digest())
    keys.add(hashlib.md5(s).hexdigest().encode())
    keys.add(hashlib.sha256(s).digest())

def plausible(d):
    return d.lstrip().startswith((b'{', b'[', b'bplist00', b'<?xml', b'\x1f\x8b', b'\x78\x9c', b'\x78\xda'))

def validate(d):
    n = d[-1] if d else 0
    if 1 <= n <= 16 and d[-n:] == bytes([n])*n: d = d[:-n]
    obj = parse(d)
    if obj is not None: return obj
    for wb in (15, 31):
        try:
            z = zlib.decompressobj(wb); raw = z.decompress(d, 8_000_000)
            if z.eof and not z.unused_data:
                obj = parse(raw)
                if obj is not None: return obj
        except zlib.error: pass
    return None

results = []
for name in ('Documents/home/detailv1', 'Documents/home/list313'):
    data = read(APP/name)
    co = collections.Counter(data)
    row = {'source': name, 'size': len(data), 'size_mod_16': len(data)%16,
           'entropy_bits_per_byte': -sum(n/len(data)*math.log2(n/len(data)) for n in co.values()),
           'direct_parse': parse(data) is not None, 'complete_compression_streams': [],
           'aes_probe_count': 0, 'validated_aes_decodings': []}
    # Only complete streams are retained, not accidental compressed signatures.
    for i in range(len(data)-1):
        if data[i:i+2] not in (b'\x78\x01', b'\x78\x9c', b'\x78\xda', b'\x1f\x8b'): continue
        try:
            z = zlib.decompressobj(31 if data[i:i+2] == b'\x1f\x8b' else 15)
            raw = z.decompress(data[i:], 8_000_000)
            if z.eof: row['complete_compression_streams'].append({'offset': i, 'length': len(raw), 'structured': parse(raw) is not None})
        except zlib.error: pass
    # Hypotheses only: no claim to have identified the proprietary cipher or key derivation.
    # Aligned headers 0/16/32/48/64; ECB; CBC zero IV, key-prefix IV, preceding-block IV.
    for key in sorted(keys):
        for offset in (0, 16, 32, 48, 64):
            ivs = [('zero', bytes(16)), ('key-prefix', key[:16])]
            if offset: ivs.append(('preceding-block', data[offset-16:offset]))
            variants = [('ECB', None)] + [('CBC-'+label, iv) for label, iv in ivs]
            for label, iv in variants:
                mode = modes.ECB() if iv is None else modes.CBC(iv)
                dec = Cipher(algorithms.AES(key), mode).decryptor()
                head = dec.update(data[offset:offset+64])
                row['aes_probe_count'] += 1
                if not plausible(head): continue
                dec = Cipher(algorithms.AES(key), mode).decryptor()
                raw = dec.update(data[offset:]) + dec.finalize()
                obj = validate(raw)
                if obj is not None:
                    row['validated_aes_decodings'].append({'mode': label, 'offset': offset, 'plaintext_sha256': sha(raw)})
                    identities(obj, name)
    results.append(row)

for name, rec in sources.items():
    rec['sha256_after'] = sha((APP/name).read_bytes())
    rec['unchanged'] = rec['sha256_before'] == rec['sha256_after']
report = {'sources_checked': len(sources), 'all_sources_unchanged': all(x['unchanged'] for x in sources.values()),
          'local_seed_count': len(seeds), 'candidate_key_count': len(keys), 'cache_probes': results,
          'decoded_resources': decoded_resources, 'identity_field_candidates': identity_fields,
          'limits': ['AES hypotheses are bounded probes, not an exhaustive decryption attempt.',
                     'No app binary, no validated cache cipher/KDF, no authenticated original plaintext.',
                     'High entropy and 16-byte alignment do not prove encryption.',
                     'No account connection, no cloud request, no key/token/plaintext export.']}
for name, obj in [('resultats.json', report), ('sources.json', sources)]:
    p = out/name; p.write_text(json.dumps(obj, ensure_ascii=False, indent=2)); p.chmod(0o600)
print(json.dumps({k: report[k] for k in ('sources_checked', 'all_sources_unchanged', 'local_seed_count', 'candidate_key_count', 'cache_probes', 'identity_field_candidates')}, ensure_ascii=False))
