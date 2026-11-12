"""Synthetic tests only: no real password or evidence content."""
import argparse
import contextlib
import csv
import importlib.util
import json
from pathlib import Path
import sqlite3
import sys
import tempfile
import types
import unittest
from unittest.mock import patch

spec=importlib.util.spec_from_file_location('triage',Path(__file__).with_name('tp02_forensic.py'))
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

class Tests(unittest.TestCase):
    def test_path_and_times(self):
        with tempfile.TemporaryDirectory() as t:
            for p in ('../escape','/absolute','a/../../escape'):
                with self.assertRaises(ValueError):m.safe(Path(t),'Domain',p)
        values=m.times(1728991800)
        self.assertTrue(any(d.isoformat()=='2024-10-15T11:30:00+00:00' for _,d in values))
        self.assertFalse(m.times('2024-10-15T13:30:00'))

    def test_signature_wal_and_raw_time(self):
        with tempfile.TemporaryDirectory() as t:
            root=Path(t)/'run';d=root/'files/Domain';d.mkdir(parents=True)
            db=d/'no_extension';c=sqlite3.connect(db)
            c.execute('PRAGMA journal_mode=WAL')
            c.execute('CREATE TABLE events(event_time INTEGER, secret TEXT)')
            c.execute('INSERT INTO events VALUES (?,?)',(1728991800,'synthetic-secret-not-to-export'));c.commit()
            before={str(p):m.sha(p) for p in d.iterdir() if p.is_file()}
            out=Path(t)/'analysis'
            m.analyze(argparse.Namespace(extracted=str(root),out=str(out),row_limit=100))
            self.assertEqual(before,{str(p):m.sha(p) for p in d.iterdir() if p.is_file()})
            with (out/'temporal-candidates.csv').open() as f: rows=list(csv.DictReader(f))
            self.assertEqual(rows[0]['raw_value'],'1728991800')
            self.assertEqual(rows[0]['central_window'],'True')
            self.assertTrue(json.loads((out/'sqlite-schema.json').read_text())[0]['wal_present'])
            self.assertNotIn('synthetic-secret-not-to-export',(out/'temporal-candidates.csv').read_text())
            c.close()

    def test_extraction_public_api_and_hashes(self):
        with tempfile.TemporaryDirectory() as t:
            base=Path(t);backup=base/'backup';fid='a'*40
            (backup/'aa').mkdir(parents=True);(backup/'aa'/fid).write_bytes(b'encrypted fixture')
            initial=m.sha(backup/'aa'/fid)
            row=dict(domain='Domain',relativePath='Documents/data',fileID=fid,flags=1,priority=1,size=9)
            inventory=base/'inventory.csv';m.write_csv(inventory,[row],list(row))
            class FakeBackup:
                def __init__(self,**kwargs):pass
                def test_decryption(self):pass
                @contextlib.contextmanager
                def manifest_db_cursor(self):
                    c=sqlite3.connect(':memory:');c.execute('CREATE TABLE Files(fileID,domain,relativePath,flags)')
                    c.execute('INSERT INTO Files VALUES (?,?,?,?)',(fid,'Domain','Documents/data',1))
                    yield c.cursor();c.close()
                def extract_file(self,**kwargs):Path(kwargs['output_filename']).write_bytes(b'plaintext')
            args=argparse.Namespace(inventory=str(inventory),backup=str(backup),out=str(base/'run'),
                max_priority=1,max_file_bytes=0,max_bytes=1000,domain=None,file_id=None,dry_run=False)
            with patch.dict(sys.modules,{'iphone_backup_decrypt':types.SimpleNamespace(EncryptedBackup=FakeBackup)}),patch.object(sys.stdin,'isatty',return_value=True),patch.object(m.getpass,'getpass',return_value='synthetic-password'):
                m.extract(args)
            log=(base/'run/extraction.jsonl').read_text();entry=json.loads(log)
            self.assertEqual(entry['status'],'ok');self.assertEqual(entry['sha256'],m.sha(base/'run/files/Domain/Documents/data'))
            self.assertEqual(initial,m.sha(backup/'aa'/fid));self.assertNotIn('synthetic-password',log)

if __name__=='__main__':unittest.main()
