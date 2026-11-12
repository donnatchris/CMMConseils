#!/usr/bin/env python3
"""Detailed follow-up to TP-03 triage: 16 October sequence and false positives."""
import collections,datetime as dt,hashlib,json,pathlib,plistlib,sqlite3,sys
from zoneinfo import ZoneInfo
from tp01_inventory import dump,sha
P=ZoneInfo('Europe/Paris');C=978307200
START=dt.datetime(2024,10,15,13,30,tzinfo=P).timestamp();END=dt.datetime(2024,10,28,19,20,tzinfo=P).timestamp()
def main():
 root=pathlib.Path(sys.argv[1]);out=root/'correlations';out.mkdir(exist_ok=False);sources=[];errors=[];res={}
 def query(rel,sql,args=()):
  p=root/'files'/rel;before=sha(p)
  try:
   c=sqlite3.connect(p.as_uri()+'?mode=ro',uri=True);c.row_factory=sqlite3.Row;r=[dict(x) for x in c.execute(sql,args)];c.close()
  except Exception as e:errors.append({'path':rel,'error':str(e)});r=[]
  sources.append({'path':rel,'before':before,'after':sha(p),'sql':sql,'parameters':args});return r
 tip='AppDomainGroup-group.com.apple.tipsnext/com.apple.MobileSMS/.tipkit/tips-store.db'
 res['tipkit_schema']=query(tip,"select name,sql from sqlite_master where type='table' and (name like 'ATRANSACTION%' or name like 'ZCORE%')")
 sql='''select t.Z_PK,t.ZTIMESTAMP,a.ZNAME author,b.ZNAME bundle,n.ZNAME context,p.ZNAME process from ATRANSACTION t left join ATRANSACTIONSTRING a on a.Z_PK=t.ZAUTHORTS left join ATRANSACTIONSTRING b on b.Z_PK=t.ZBUNDLEIDTS left join ATRANSACTIONSTRING n on n.Z_PK=t.ZCONTEXTNAMETS left join ATRANSACTIONSTRING p on p.Z_PK=t.ZPROCESSIDTS where t.ZTIMESTAMP between ? and ? order by t.ZTIMESTAMP'''
 res['tipkit']=query(tip,sql,(START-C,END-C))
 res['tipkit_rules']=query(tip,'select Z_PK,ZLASTEVALUATED from ZCORERULERECORD where ZLASTEVALUATED between ? and ?',(START-C,END-C))
 pa='HomeDomain/Library/Accessibility/com.apple.personalaudio.sqlite'
 res['personalaudio']=query(pa,'select Z_PK,ZSTARTEDAT,ZENDEDAT from ANSCKEVENT where ZSTARTEDAT between ? and ? or ZENDEDAT between ? and ?',(START-C,END-C,START-C,END-C))
 pg='AppDomainGroup-group.com.apple.PegasusConfiguration/AlpsWarehouse/data_warehouse.db'
 res['warehouse_schema']=query(pg,"select sql from sqlite_master where name='spotlight_sfm'")
 res['warehouse']=query(pg,'select rowid,timestamp from spotlight_sfm where timestamp between ? and ? order by timestamp',(START,END))
 # Dates and structure only, never key material.
 for p in (root/'files/AppDomainGroup-group.com.facebook.Facebook').rglob('*.db'):
  rel=str(p.relative_to(root/'files'))
  schema=query(rel,"select sql from sqlite_master where name='ohai_gateway_key_configs'")
  if schema:res['facebook_schema']=schema;res['facebook_dates']=query(rel,'select rowid,last_updated_time from ohai_gateway_key_configs where last_updated_time between ? and ?',(START,END));break
 res['tcc']=query('HomeDomain/Library/TCC/TCC.db','select service,client,auth_value,auth_reason,last_modified from access where last_modified between ? and ?',(START,END))
 res['keyboard_schema']=query('KeyboardDomain/Library/Keyboard/user_model_database.sqlite',"select sql from sqlite_master where name='usermodeldurablerecords'")
 # Validate logical Health identity against preferences and compare the two Mini.
 h=root/'files/HomeDomain/Library/Preferences/com.apple.healthd.plist';v=plistlib.loads(h.read_bytes()).get('SyncIdentityHardwareIdentifier');ident=query('HealthDomain/Health/healthdb.sqlite','select ROWID,hex(hardware_identifier) hardware_hex from sync_identities')
 res['health_identity']={'preference_sha256':sha(h),'hardware_identifier_sha256':hashlib.sha256(v).hexdigest() if isinstance(v,bytes) else None,'matching_rows':[x['ROWID'] for x in ident if isinstance(v,bytes) and bytes.fromhex(x['hardware_hex'])==v]}
 # Record all candidate counts by type, without a medical quantity.
 dump(out/'results.json',res);dump(out/'sources.json',sources);dump(out/'errors.json',errors);print(json.dumps({'tipkit':len(res['tipkit']),'errors':len(errors)}))
if __name__=='__main__':main()
