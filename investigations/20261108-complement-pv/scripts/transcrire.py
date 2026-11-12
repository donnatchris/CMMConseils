from faster_whisper import WhisperModel
from pathlib import Path
import json,hashlib,subprocess,numpy as np
base=Path('investigations/20261108-complement-pv')
model=WhisperModel('small',device='cpu',compute_type='int8',download_root='/tmp/cmm-whisper-models',cpu_threads=4)
p=base/'prive/salon-audio.mp3'
pcm=subprocess.run(['ffmpeg','-v','error','-i',str(p),'-f','f32le','-ar','16000','-ac','1','-'],capture_output=True,check=True).stdout
segments,info=model.transcribe(np.frombuffer(pcm,dtype=np.float32),language='fr',beam_size=5,vad_filter=True,condition_on_previous_text=False)
rows=[]
with (base/'prive/transcription-automatique.jsonl').open('x') as f:
 for s in segments:
  r={'start':s.start,'end':s.end,'text':s.text,'avg_logprob':s.avg_logprob,'no_speech_prob':s.no_speech_prob}
  rows.append(r);f.write(json.dumps(r,ensure_ascii=False)+'\n');f.flush()
(base/'resultats/transcription-meta.json').write_text(json.dumps({'model':'small','engine':'faster-whisper','language':'fr','vad_filter':True,'condition_on_previous_text':False,'segments':len(rows),'audio_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'duration':info.duration,'status':'automatic_unverified_not_a_verbatim_transcript'},indent=2))
print('segments',len(rows))
