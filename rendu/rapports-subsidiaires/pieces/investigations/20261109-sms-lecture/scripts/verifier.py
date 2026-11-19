"""Lecture seule ciblée ; extraction limitée aux trois chaînes UTF-8 observées.

Ce script ne constitue pas un décodeur général de NSAttributedString/typedstream.
Les codes et identifiants d'expéditeurs ne sont pas exportés.
"""
from pathlib import Path
import csv
import hashlib
import json
import re
import sqlite3
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

root = Path(__file__).resolve().parents[3]
base = Path(__file__).resolve().parents[1]
source = root / 'telephones/recherche-TP-02/extraction-systeme-20261014/files/HomeDomain/Library/SMS/sms.db'
sources = [source, Path(str(source)+'-wal'), Path(str(source)+'-shm')]
def hashes():
    return {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest() for p in sources if p.exists()}
before = hashes()
connection = sqlite3.connect(source.as_uri()+'?mode=ro&immutable=1', uri=True)
connection.row_factory = sqlite3.Row
epoch = datetime(2001, 1, 1, tzinfo=timezone.utc)
def paris(ns):
    return (epoch + timedelta(microseconds=ns//1000)).astimezone(ZoneInfo('Europe/Paris')).isoformat(timespec='microseconds')
messages = []
for row in connection.execute('SELECT ROWID,date,date_read,is_read,ck_sync_state,handle_id,attributedBody FROM message WHERE ROWID BETWEEN 74688 AND 74690 ORDER BY ROWID'):
    body = row['attributedBody']
    marker = b'\x01\x95\x84\x01+'
    assert body.count(marker) == 1
    position = body.index(marker) + len(marker)
    length = body[position]
    assert length < 128  # Only the observed short-string encoding is handled.
    start = position + 1
    raw = body[start:start+length]
    assert body[start+length] == 0x86
    text = raw.decode('utf-8')
    if row['ROWID'] == 74688:
        assert re.fullmatch(r'Utiliser \d{6} comme code de réinitialisation de mot de passe Microsoft', text)
        nature = 'Code de réinitialisation de mot de passe Microsoft'
    else:
        assert re.fullmatch(r'G-\d{6} est votre code de validation Google\. Ne le partagez avec personne\.', text)
        nature = 'Code de validation Google'
    handle = connection.execute('SELECT id FROM handle WHERE ROWID=?', (row['handle_id'],)).fetchone()
    messages.append(dict(rowid=row['ROWID'],date=row['date'],date_read=row['date_read'],
        date_paris=paris(row['date']),date_read_paris=paris(row['date_read']),
        delay_ns=row['date_read']-row['date'],is_read=row['is_read'],ck_sync_state=row['ck_sync_state'],
        nature=nature,body_sha256=hashlib.sha256(body).hexdigest(),utf8_offset=start,utf8_length=length,
        sender_handle_present=bool(handle and handle[0]),sender_identity_verified=False))
connection.close()
timeline = root / 'telephones/recherche-TP-02/approfondissement-activite-202410/timeline-correlated.csv'
nearby = []
with timeline.open() as stream:
    for event in csv.DictReader(stream):
        if not event['paris']:
            continue
        instant = datetime.fromisoformat(event['paris'])
        if any(abs((instant-datetime.fromisoformat(m['date_read_paris'])).total_seconds()) <= 60 for m in messages):
            nearby.append({k:event[k] for k in ('paris','relativePath','locator','observation','interpretation')})
after = hashes()
assert before == after
result = dict(messages=messages,source_hashes_before=before,source_hashes_after=after,
    timeline_sha256=hashlib.sha256(timeline.read_bytes()).hexdigest(),
    nearby_events_within_60_seconds=nearby,
    limits=['Extraction ciblée des chaînes ; pas de décodage général des archives.',
        'Marques Microsoft/Google issues du corps, expéditeur non authentifié.',
        'ck_sync_state brut ne date pas une synchronisation et ne désigne pas un appareil.',
        'Corrélation limitée à la chronologie existante ; aucune nouvelle recherche exhaustive des journaux.'])
(base/'resultats/verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(messages=len(messages),source_hashes_unchanged=before==after,nearby_events=len(nearby))))
