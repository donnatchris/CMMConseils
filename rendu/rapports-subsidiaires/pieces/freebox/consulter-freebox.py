"""Consultations autorisées Freebox, secrets en mémoire, destination neuve."""
import argparse
import getpass
import hashlib
import hmac
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.parse import urlsplit


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base-url', required=True)
    parser.add_argument('--app-id', required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    if urlsplit(args.base_url).scheme != 'https':
        parser.error('Une base HTTPS est requise.')
    args.out.mkdir(parents=True, exist_ok=False)
    app_token = getpass.getpass('App token (non enregistré) : ')
    session_token = None

    def call(endpoint, payload=None):
        headers = {'Content-Type': 'application/json'}
        if session_token:
            headers['X-Fbx-App-Auth'] = session_token
        request = Request(args.base_url.rstrip('/') + '/' + endpoint,
                          data=None if payload is None else json.dumps(payload).encode(),
                          headers=headers)
        with urlopen(request, timeout=30) as response:
            raw = response.read()
        result = json.loads(raw)
        if not result.get('success'):
            raise RuntimeError('Échec API : ' + str(result.get('error_code', 'inconnu')))
        return result, raw

    challenge = call('login/')[0]['result']['challenge']
    password = hmac.new(app_token.encode(), challenge.encode(), hashlib.sha1).hexdigest()
    session_token = call('login/session/', {'app_id': args.app_id, 'password': password})[0]['result']['session_token']
    records = []
    try:
        for endpoint, name in [('system/', 'system.json'), ('lan/browser/pub/', 'lan.json')]:
            result, raw = call(endpoint)
            destination = args.out / name
            destination.write_bytes(raw)
            records.append({'endpoint': endpoint, 'utc': datetime.now(timezone.utc).isoformat(),
                            'file': name, 'sha256': hashlib.sha256(raw).hexdigest()})
    finally:
        call('login/logout/', {})
        (args.out / 'manifest.json').write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n')


if __name__ == '__main__':
    main()
