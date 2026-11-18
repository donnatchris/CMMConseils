# Paramètres et commandes conservés après comparaison des versions

Annexe technique de la révision du 18 novembre 2026. Les sources historiques sont récupérables par le registre Git ; leurs anciennes conclusions ne sont pas reprises. Les blocs ci-dessous conservent les informations utiles absentes de la référence rédactionnelle actuelle. Ils ne sont pas des commandes exécutées par cette révision. Les chemins de sorties sont historiques : pour une reproduction, utiliser une copie de travail et une destination nouvelle après lecture du script ; ne jamais écrire dans les acquisitions ni les résultats conservés. Les commandes PowerShell de retrait d’application sont des traces examinées, pas des instructions de reproduction.


## Bloc 1 — freebox/analyse-freebox.md

Provenance Git : `investigations/20261017-recroisements/rapports-avant/freebox/analyse-freebox.md` (voir registre de récupération).

```text
# Échantillon d'examen de fichier vidéo avec mediainfo
General
ID                                       : 45770 (0xB2CA)
Format                                   : BDAV
Format/Info                              : Blu-ray Video
File size                                : 695 MiB
Duration                                 : 49 min 44 s
Overall bit rate mode                    : Variable
Overall bit rate                         : 1 953 kb/s
Frame rate                               : 25.000 FPS

Video
ID                                       : 120 (0x78)
Menu ID                                  : 45770 (0xB2CA)
Format                                   : AVC
Format/Info                              : Advanced Video Codec
Format profile                           : High@L4
Format settings                          : CABAC / 4 Ref Frames
Codec ID                                 : 27
Duration                                 : 49 min 43 s
Width                                    : 720 pixels
Height                                   : 576 pixels
Display aspect ratio                     : 16:9
Frame rate                               : 25.000 FPS
Standard                                 : PAL
Color space                              : YUV
Chroma subsampling                       : 4:2:0
Bit depth                                : 8 bits
Scan type                                : MBAFF
Scan order                               : Top Field First

Audio #1
ID                                       : 130 (0x82)
Format                                   : AAC LC
Format/Info                              : Advanced Audio Codec Low Complexity
Format version                           : Version 2
Muxing mode                              : ADTS
Codec ID                                 : 15-2
Duration                                 : 49 min 44 s
Bit rate mode                            : Variable
Channel(s)                               : 2 channels
Channel layout                           : L R
Sampling rate                            : 48.0 kHz
Frame rate                               : 46.875 FPS (1024 SPF)
Compression mode                         : Lossy
Delay relative to video                  : -507 ms
Language                                 : French

Audio #2
ID                                       : 131 (0x83)
Format                                   : AAC LC SBR
Commercial name                          : HE-AAC
Format version                           : Version 2
Format settings                          : Implicit
Muxing mode                              : ADTS
Codec ID                                 : 15-2
Duration                                 : 49 min 44 s
Bit rate mode                            : Variable
Channel(s)                               : 2 channels
Channel layout                           : L R
Sampling rate                            : 48.0 kHz
Frame rate                               : 23.438 FPS (2048 SPF)
Compression mode                         : Lossy
Delay relative to video                  : -195 ms
Language                                 : qaa

Audio #3
ID                                       : 132 (0x84)
Format                                   : AAC LC SBR
Commercial name                          : HE-AAC
Format version                           : Version 2
Format settings                          : Implicit
Muxing mode                              : ADTS
Codec ID                                 : 15-2
Duration                                 : 49 min 43 s
Bit rate mode                            : Variable
Channel(s)                               : 2 channels
Channel layout                           : L R
Sampling rate                            : 48.0 kHz
Frame rate                               : 23.438 FPS (2048 SPF)
Compression mode                         : Lossy
Delay relative to video                  : -299 ms
Language                                 : qad

Text #1
ID                                       : 140 (0x8C)-888
Format                                   : Teletext Subtitle
Language                                 : French
Language, more info                      : For hearing impaired people

Text #2
ID                                       : 140 (0x8C)-889
Format                                   : Teletext Subtitle
Language                                 : French
```


## Bloc 9 — ordinateur/analyse-ordinateur.md

Provenance Git : `investigations/20261017-recroisements/rapports-avant/ordinateur/analyse-ordinateur.md` (voir registre de récupération).

```text
OP01.E01 … OP01.E74
  → ewfmount : /mnt/ewf/ewf1 (vue du disque physique)
  → loop en lecture seule : /dev/loop14, partition /dev/loop14p3
  → dislocker -r : /mnt/dislocker/dislocker-file (vue NTFS déchiffrée)
  → ntfs-3g -o ro,norecover : /mnt/windows
```


## Bloc 10 — ordinateur/analyse-ordinateur.md

Provenance Git : `investigations/20261017-recroisements/rapports-avant/ordinateur/analyse-ordinateur.md` (voir registre de récupération).

```bash
ssh -t -F /home/chris/.ssh/config sift
```


## Bloc 11 — ordinateur/analyse-ordinateur.md

Provenance Git : `investigations/20261017-recroisements/rapports-avant/ordinateur/analyse-ordinateur.md` (voir registre de récupération).

```bash
findmnt /media/shared
findmnt /mnt/ewf
findmnt /mnt/dislocker
findmnt /mnt/windows
sudo losetup -l
sudo ls /mnt/windows/Windows/System32/winevt/Logs/System.evtx
```


## Bloc 12 — ordinateur/analyse-ordinateur.md

Provenance Git : `investigations/20261017-recroisements/rapports-avant/ordinateur/analyse-ordinateur.md` (voir registre de récupération).

```bash
sudo mkdir -p /mnt/ewf /mnt/dislocker /mnt/windows
sudo ewfmount /media/shared/forensic/SADEDINE-2026/OP-01/OP01.E01 /mnt/ewf
sudo mmls /mnt/ewf/ewf1
sudo blkid -p -O 290455552 /mnt/ewf/ewf1

OP01_LOOP=$(sudo losetup -fP --read-only --show /mnt/ewf/ewf1)
sudo lsblk -o NAME,SIZE,FSTYPE,RO,TYPE,MOUNTPOINT "$OP01_LOOP"
sudo dislocker -r -V "${OP01_LOOP}p3" -p -- /mnt/dislocker
sudo mount -t ntfs-3g -o ro,norecover \
  /mnt/dislocker/dislocker-file /mnt/windows
findmnt /mnt/windows
sudo losetup -l "$OP01_LOOP"
```


## Bloc 13 — ordinateur/analyse-ordinateur.md

Provenance Git : `investigations/20261017-recroisements/rapports-avant/ordinateur/analyse-ordinateur.md` (voir registre de récupération).

```bash
ewfinfo /media/shared/forensic/SADEDINE-2026/OP-01/OP01.E01
# Contrôle complémentaire proposé ; non exécuté dans les travaux rapportés :
sudo ewfverify /media/shared/forensic/SADEDINE-2026/OP-01/OP01.E01
```


## Bloc 14 — ordinateur/analyse-ordinateur.md

Provenance Git : `investigations/20261017-recroisements/rapports-avant/ordinateur/analyse-ordinateur.md` (voir registre de récupération).

```powershell
Get-AppxPackage C27EB4BA.DropboxOEM | Remove-AppxPackage
Get-AppxProvisionedPackage -Online |
  Where-Object DisplayName -In "C27EB4BA.DropboxOEM" |
  Remove-ProvisionedAppxPackage -Online
```


## Bloc 15 — ordinateur/analyse-ordinateur.md

Provenance Git : `investigations/20261017-recroisements/rapports-avant/ordinateur/analyse-ordinateur.md` (voir registre de récupération).

```bash
df -h /tmp
command -v evtxexport evtxinfo vshadowinfo
python3 -c 'import pyevtx,pyregf,pyfsntfs,pyscca,pylnk,sqlite3'

sudo evtxinfo /mnt/windows/Windows/System32/winevt/Logs/System.evtx
sudo evtxinfo /mnt/windows/Windows/System32/winevt/Logs/Security.evtx
sudo evtxexport -f xml /mnt/windows/Windows/System32/winevt/Logs/System.evtx
sudo evtxexport -f xml /mnt/windows/Windows/System32/winevt/Logs/Security.evtx
# Tentative de récupération offerte par le même outil :
sudo evtxexport -m recovered -f xml \
  /mnt/windows/Windows/System32/winevt/Logs/System.evtx
```


## Bloc 16 — ordinateur/analyse-ordinateur.md

Provenance Git : `investigations/20261017-recroisements/rapports-avant/ordinateur/analyse-ordinateur.md` (voir registre de récupération).

```bash
sudo ntfsinfo -f -F '/$Extend/$UsnJrnl' /mnt/dislocker/dislocker-file
sudo ntfscat -f -n '$Max' /mnt/dislocker/dislocker-file '/$Extend/$UsnJrnl'
sudo vshadowinfo /mnt/dislocker/dislocker-file
```


## Bloc 17 — ordinateur/analyse-ordinateur.md

Provenance Git : `investigations/20261017-recroisements/rapports-avant/ordinateur/analyse-ordinateur.md` (voir registre de récupération).

```bash
cd "$(git rev-parse --show-toplevel)"
OP01_SCRIPTS="$PWD/ordinateur/recherche-OP-01"
OP01_REPRO=$(mktemp -d /tmp/OP-01-reproduction.XXXXXX)
mkdir -p "$OP01_REPRO/evtx" "$OP01_REPRO/reveil-16oct" \
  "$OP01_REPRO/integrite-evtx"
cp -a "$OP01_SCRIPTS/scripts" "$OP01_REPRO/"
cp -a "$OP01_SCRIPTS/reveil-16oct/scripts" "$OP01_REPRO/reveil-16oct/"
cp -a "$OP01_SCRIPTS/integrite-evtx/scripts" "$OP01_REPRO/integrite-evtx/"
```


## Bloc 18 — ordinateur/analyse-ordinateur.md

Provenance Git : `investigations/20261017-recroisements/rapports-avant/ordinateur/analyse-ordinateur.md` (voir registre de récupération).

```bash
ssh -F /home/chris/.ssh/config sift 'python3 -' \
  < "$OP01_SCRIPTS/scripts/evtx_scan.py" > "$OP01_REPRO/scan.log"
ssh -F /home/chris/.ssh/config sift 'python3 -' \
  < "$OP01_SCRIPTS/scripts/check_xml_errors.py" \
  > "$OP01_REPRO/xml-errors-scan.log"
```


## Bloc 19 — ordinateur/analyse-ordinateur.md

Provenance Git : `investigations/20261017-recroisements/rapports-avant/ordinateur/analyse-ordinateur.md` (voir registre de récupération).

```bash
ssh -F /home/chris/.ssh/config sift 'python3 -' \
  < "$OP01_SCRIPTS/reveil-16oct/scripts/collect_wake.py" \
  > "$OP01_REPRO/reveil-16oct/collect.log"
ssh -F /home/chris/.ssh/config sift 'python3 -' \
  < "$OP01_SCRIPTS/reveil-16oct/scripts/search_wake_mentions.py" \
  > "$OP01_REPRO/reveil-16oct/search.log"
```


## Bloc 20 — ordinateur/analyse-ordinateur.md

Provenance Git : `investigations/20261017-recroisements/rapports-avant/ordinateur/analyse-ordinateur.md` (voir registre de récupération).

```bash
ssh -F /home/chris/.ssh/config sift 'python3 -' \
  < "$OP01_SCRIPTS/integrite-evtx/scripts/audit_evtx.py" \
  > "$OP01_REPRO/integrite-evtx/audit.log"
ssh -F /home/chris/.ssh/config sift 'python3 -' \
  < "$OP01_SCRIPTS/integrite-evtx/scripts/recover_audit.py" \
  > "$OP01_REPRO/integrite-evtx/recovery.log"
ssh -F /home/chris/.ssh/config sift 'python3 -' \
  < "$OP01_SCRIPTS/integrite-evtx/scripts/independent.py" \
  > "$OP01_REPRO/integrite-evtx/independent.log"
```


## Bloc 21 — ordinateur/analyse-ordinateur.md

Provenance Git : `investigations/20261017-recroisements/rapports-avant/ordinateur/analyse-ordinateur.md` (voir registre de récupération).

```bash
ssh -F /home/chris/.ssh/config sift 'sudo -n python3 -' \
  < "$OP01_SCRIPTS/integrite-evtx/scripts/usn.py" \
  > "$OP01_REPRO/integrite-evtx/usn.log"
ssh -F /home/chris/.ssh/config sift 'sudo -n python3 -' \
  < "$OP01_SCRIPTS/integrite-evtx/scripts/vss_catalog.py" \
  > "$OP01_REPRO/integrite-evtx/vss.log"
ssh -F /home/chris/.ssh/config sift 'sudo -n python3 -' \
  < "$OP01_SCRIPTS/integrite-evtx/scripts/mft_scan.py" \
  > "$OP01_REPRO/integrite-evtx/mft-scan.log"
ssh -F /home/chris/.ssh/config sift 'sudo -n python3 -' \
  < "$OP01_SCRIPTS/integrite-evtx/scripts/mft_crosscheck.py" \
  > "$OP01_REPRO/integrite-evtx/mft-crosscheck.log"
ssh -F /home/chris/.ssh/config sift 'sudo -n python3 -' \
  < "$OP01_SCRIPTS/integrite-evtx/scripts/deleted_evtx.py" \
  > "$OP01_REPRO/integrite-evtx/deleted-evtx.log"
ssh -F /home/chris/.ssh/config sift 'sudo -n python3 -' \
  < "$OP01_SCRIPTS/integrite-evtx/scripts/decode_deleted_chunks.py" \
  > "$OP01_REPRO/integrite-evtx/deleted-decode.log"
```


## Bloc 22 — ordinateur/analyse-ordinateur.md

Provenance Git : `investigations/20261017-recroisements/rapports-avant/ordinateur/analyse-ordinateur.md` (voir registre de récupération).

```bash
set -o pipefail
ssh -F /home/chris/.ssh/config sift \
  'tar -C /tmp/OP-01-scelles-20261013 -cf - .' \
  | tar -xf - -C "$OP01_REPRO"
ssh -F /home/chris/.ssh/config sift \
  'tar -C /tmp/OP-01-reveil-20261013 -cf - .' \
  | tar -xf - -C "$OP01_REPRO/reveil-16oct"
ssh -F /home/chris/.ssh/config sift \
  'tar -C /tmp/OP-01-integrite-20261013 -cf - .' \
  | tar -xf - -C "$OP01_REPRO/integrite-evtx"
```


## Bloc 23 — ordinateur/analyse-ordinateur.md

Provenance Git : `investigations/20261017-recroisements/rapports-avant/ordinateur/analyse-ordinateur.md` (voir registre de récupération).

```bash
ssh -F /home/chris/.ssh/config sift \
  'tar -C /mnt/windows/Windows/System32/winevt/Logs -cf - System.evtx Security.evtx Application.evtx OAlerts.evtx Microsoft-Windows-Winlogon%4Operational.evtx Microsoft-Windows-TerminalServices-LocalSessionManager%4Operational.evtx "Windows PowerShell.evtx" Microsoft-Windows-PowerShell%4Operational.evtx' \
  | tar -xf - -C "$OP01_REPRO/evtx"

python3 "$OP01_REPRO/reveil-16oct/scripts/summarize_wake.py"
python3 "$OP01_REPRO/integrite-evtx/scripts/query_firefox.py"
python3 "$OP01_REPRO/integrite-evtx/scripts/usn_cloud_crosscheck.py"
python3 "$OP01_REPRO/scripts/summarize.py"
```


## Bloc 24 — ordinateur/analyse-ordinateur.md

Provenance Git : `investigations/20261017-recroisements/rapports-avant/ordinateur/analyse-ordinateur.md` (voir registre de récupération).

```bash
cd "$(git rev-parse --show-toplevel)/ordinateur/recherche-OP-01"
sha256sum -c SHA256SUMS
```


## Bloc 25 — ordinateur/analyse-ordinateur.md

Provenance Git : `investigations/20261017-recroisements/rapports-avant/ordinateur/analyse-ordinateur.md` (voir registre de récupération).

```bash
scp -F /home/chris/.ssh/config \
  ordinateur/recherche-OP-01/extractions-acces/scripts/{collect_phase2,amcache_srum,archives,l16b_mft,followup,mft_targets,source_matches,mbox_name_search}.py \
  sift:/home/sansforensics/

ssh -F /home/chris/.ssh/config sift \
  'python3 /home/sansforensics/collect_phase2.py && python3 /home/sansforensics/amcache_srum.py'
ssh -F /home/chris/.ssh/config sift \
  'python3 /home/sansforensics/archives.py && python3 /home/sansforensics/l16b_mft.py && python3 /home/sansforensics/followup.py && python3 /home/sansforensics/mft_targets.py && python3 /home/sansforensics/source_matches.py && python3 /home/sansforensics/mbox_name_search.py'

set -o pipefail
ssh -F /home/chris/.ssh/config sift \
  'tar -C /home/sansforensics/analysis/OP-01/extractions-acces-20261013 -cf - .' \
  | tar -xf - -C ordinateur/recherche-OP-01/extractions-acces

python3 ordinateur/recherche-OP-01/extractions-acces/scripts/firefox_history.py
python3 ordinateur/recherche-OP-01/extractions-acces/scripts/setupapi_usb.py
python3 ordinateur/recherche-OP-01/extractions-acces/scripts/usb_mapping.py
python3 ordinateur/recherche-OP-01/extractions-acces/scripts/tasks_index.py
python3 ordinateur/recherche-OP-01/extractions-acces/scripts/summarize_phase2.py
python3 ordinateur/recherche-OP-01/extractions-acces/scripts/validate_sources.py
```


## Bloc 26 — ordinateur/analyse-ordinateur.md

Provenance Git : `investigations/20261017-recroisements/rapports-avant/ordinateur/analyse-ordinateur.md` (voir registre de récupération).

```text
ZIP supprimé (MFT 76808)
03a593ea508aefdb1bf8b0280dce839a1b7f8098a7560a3f8c345a61d7a5bc44
DOCX supprimé (MFT 77995)
38fcaf9ab9a8aac80038dd0bd75a45e884339208def6d083d6134473becf2b0a
```


## Bloc 27 — ordinateur/analyse-ordinateur.md

Provenance Git : `investigations/20261017-recroisements/rapports-avant/ordinateur/analyse-ordinateur.md` (voir registre de récupération).

```bash
scp -F /home/chris/.ssh/config \
  ordinateur/recherche-OP-01/fichiers-supprimes/scripts/{inventory_mft,triage,recover,analyze_recovered,compare_drive,static_checks,review_pe_hits,retry_compressed}.py \
  sift:/home/sansforensics/

ssh -F /home/chris/.ssh/config sift \
  'sudo -n python3 /home/sansforensics/inventory_mft.py && python3 /home/sansforensics/triage.py'
ssh -F /home/chris/.ssh/config sift \
  'sudo -n python3 /home/sansforensics/recover.py && sudo -n python3 /home/sansforensics/analyze_recovered.py'
ssh -F /home/chris/.ssh/config sift \
  'sudo -n python3 /home/sansforensics/compare_drive.py && sudo -n python3 /home/sansforensics/static_checks.py && sudo -n python3 /home/sansforensics/review_pe_hits.py && sudo -n python3 /home/sansforensics/retry_compressed.py'
```


## Bloc 28 — ordinateur/analyse-ordinateur.md

Provenance Git : `investigations/20261017-recroisements/rapports-avant/ordinateur/analyse-ordinateur.md` (voir registre de récupération).

```bash
ssh -F /home/chris/.ssh/config sift \
  'set -o pipefail; sudo -n icat /mnt/dislocker/dislocker-file 76808 | sha256sum'
ssh -F /home/chris/.ssh/config sift \
  'set -o pipefail; sudo -n icat /mnt/dislocker/dislocker-file 77995 | sha256sum'
ssh -F /home/chris/.ssh/config sift \
  'set -o pipefail; sudo -n icat /mnt/dislocker/dislocker-file 166334 | sha256sum'
```


## Bloc 29 — ordinateur/analyse-ordinateur.md

Provenance Git : `investigations/20261017-recroisements/rapports-avant/ordinateur/analyse-ordinateur.md` (voir registre de récupération).

```bash
mkdir -p /tmp/OP01-reproduction-supprimes
set -o pipefail
ssh -F /home/chris/.ssh/config sift \
  'sudo -n tar -C /home/sansforensics/analysis/OP-01/fichiers-supprimes-20261013 -cf - --exclude=mft-selection-unresolved.jsonl .' \
  | tar -xf - -C /tmp/OP01-reproduction-supprimes

python3 ordinateur/recherche-OP-01/fichiers-supprimes/scripts/local_reviews.py
python3 ordinateur/recherche-OP-01/fichiers-supprimes/scripts/summarize_deleted.py
```


## Bloc 30 — telephones/analyse-TP-02.md

Provenance Git : `investigations/20261017-recroisements/rapports-avant/telephones/analyse-TP-02.md` (voir registre de récupération).

```text
Sauvegarde chiffrée :
/mnt/data/forensic/SADEDINE-2026/TP-02/00008110-001C69A002BA801E/

Manifeste déchiffré contrôlé :
/mnt/data/forensic/SADEDINE-2026/ANALYSES/TP-02/Manifest-decrypted.db
```


## Bloc 31 — telephones/analyse-TP-02.md

Provenance Git : `investigations/20261017-recroisements/rapports-avant/telephones/analyse-TP-02.md` (voir registre de récupération).

```text
Media/PhotoData/Thumbnails/VideoKeyFrames/DCIM/101APPLE/IMG_1773.MP4/LocalVideoKeyFrame.jpg
```


## Bloc 32 — telephones/analyse-TP-02.md

Provenance Git : `investigations/20261017-recroisements/rapports-avant/telephones/analyse-TP-02.md` (voir registre de récupération).

```bash
python3 telephones/scripts/tp02_forensic.py inventory --out /tmp/TP02-inventaire-reproduction

# Extraction interactive ciblée : le mot de passe n’est pas un argument.
telephones/scripts/.venv-iphone/bin/python telephones/scripts/tp02_forensic.py extract \
  --inventory telephones/recherche-TP-02/selection-complements.csv \
  --max-priority 2 --out /tmp/TP02-complements-reproduction

python3 telephones/scripts/tp02_forensic.py analyze \
  --extracted /tmp/TP02-complements-reproduction \
  --out /tmp/TP02-analyse-reproduction --row-limit 1000000

python3 telephones/scripts/tp02_media_metadata.py \
  --extracted telephones/recherche-TP-02/extraction-medias-20261014 \
  --out /tmp/TP02-exif-reproduction.json

python3 telephones/scripts/tp02_consistency.py \
  --extracted telephones/recherche-TP-02/extraction-cameras-20261014 \
  --extracted telephones/recherche-TP-02/extraction-systeme-20261014 \
  --extracted telephones/recherche-TP-02/extraction-complements-20261014 \
  --extracted telephones/recherche-TP-02/extraction-medias-20261014 \
  --out /tmp/TP02-coherence-reproduction.json
```


## Bloc 33 — telephones/analyse-TP-02.md

Provenance Git : `investigations/20261017-recroisements/rapports-avant/telephones/analyse-TP-02.md` (voir registre de récupération).

```bash
python3 telephones/scripts/tp02_activity_oct2024.py --out /tmp/TP02-activite-reproduction
python3 telephones/scripts/tp02_activity_correlations.py --out /tmp/TP02-activite-reproduction
python3 telephones/scripts/tp02_activity_verify.py \
  --out telephones/recherche-TP-02/approfondissement-activite-202410 \
  --reproduction /tmp/TP02-activite-reproduction
```


## Bloc 34 — telephones/analyse-TP-02.md

Provenance Git : `investigations/20261017-recroisements/rapports-avant/telephones/analyse-TP-02.md` (voir registre de récupération).

```bash
python3 telephones/scripts/tp02_wifi17_investigation.py --out /tmp/TP02-wifi17-reproduction
python3 telephones/scripts/tp02_wifi17_crosschecks.py --out /tmp/TP02-wifi17-reproduction
```


## Bloc 35 — cartes_sd/analyse-cartes_sd-SD-01.md

Provenance Git : `investigations/20261019-retour-cliente/rapports-avant/cartes_sd/analyse-cartes_sd-SD-01.md` (voir registre de récupération).

```bash
ssh -F /home/chris/.ssh/config sift 'sudo -n ewfverify -q /media/shared/forensic/SADEDINE-2026/ANALYSES/SD-01/SD01.E01'
ssh -F /home/chris/.ssh/config sift 'sudo -n mmls /mnt/ewf-sd01/ewf1'
ssh -F /home/chris/.ssh/config sift 'sudo -n fsstat -o 8192 /mnt/ewf-sd01/ewf1'
ssh -F /home/chris/.ssh/config sift 'sudo -n fls -o 8192 -r -p /mnt/ewf-sd01/ewf1'
ssh -F /home/chris/.ssh/config sift 'sudo -n fls -o 8192 -r -d -p /mnt/ewf-sd01/ewf1'
ssh -F /home/chris/.ssh/config sift 'sudo -n istat -z UTC -o 8192 /mnt/ewf-sd01/ewf1 1543'
ssh -F /home/chris/.ssh/config sift 'sudo -n icat -r -o 8192 /mnt/ewf-sd01/ewf1 1543'
ssh -F /home/chris/.ssh/config sift 'sudo -n icat -o 8192 /mnt/ewf-sd01/ewf1 76861460'
```


## Bloc 36 — cartes_sd/analyse-cartes_sd-SD-02.md

Provenance Git : `investigations/20261019-retour-cliente/rapports-avant/cartes_sd/analyse-cartes_sd-SD-02.md` (voir registre de récupération).

```text
/media/shared/forensic/SADEDINE-2026/ANALYSES/SD-02/
```


## Bloc 37 — cartes_sd/analyse-cartes_sd-SD-02.md

Provenance Git : `investigations/20261019-retour-cliente/rapports-avant/cartes_sd/analyse-cartes_sd-SD-02.md` (voir registre de récupération).

```text
CAMERA TERRASSE/.record_tmp/20241112_234855_10.mp4        6 135 808 octets
CAMERA TERRASSE/.record_tmp/20241112_234855_10.mp4.moov       1 006 octets
CAMERA TERRASSE/.record_tmp/20241112_234855_10.mp4.stbl      24 824 octets
```


## Bloc 38 — cartes_sd/analyse-cartes_sd-SD-02.md

Provenance Git : `investigations/20261019-retour-cliente/rapports-avant/cartes_sd/analyse-cartes_sd-SD-02.md` (voir registre de récupération).

```bash
ssh -F /home/chris/.ssh/config sift \
  'sudo -n ewfverify -q -d sha256 /media/shared/forensic/SADEDINE-2026/ANALYSES/SD-02/SD02.E01'
ssh -F /home/chris/.ssh/config sift 'sudo -n mmls /mnt/ewf-sd02/ewf1'
ssh -F /home/chris/.ssh/config sift 'sudo -n fsstat -o 8192 /mnt/ewf-sd02/ewf1'
ssh -F /home/chris/.ssh/config sift 'sudo -n fls -o 8192 -r -p /mnt/ewf-sd02/ewf1'
ssh -F /home/chris/.ssh/config sift 'sudo -n istat -z UTC -o 8192 /mnt/ewf-sd02/ewf1 1072'
ssh -F /home/chris/.ssh/config sift 'sudo -n icat -r -o 8192 /mnt/ewf-sd02/ewf1 575101256'
```


## Bloc 39 — cartes_sd/analyse-cartes_sd-SD-03.md

Provenance Git : `investigations/20261019-retour-cliente/rapports-avant/cartes_sd/analyse-cartes_sd-SD-03.md` (voir registre de récupération).

```text
/media/shared/forensic/SADEDINE-2026/ANALYSES/SD-03/SD03.E01 à SD03.E12
```


## Bloc 40 — cartes_sd/analyse-cartes_sd-SD-03.md

Provenance Git : `investigations/20261019-retour-cliente/rapports-avant/cartes_sd/analyse-cartes_sd-SD-03.md` (voir registre de récupération).

```bash
ssh -F /home/chris/.ssh/config sift 'sudo -n ewfverify -q -d sha256 /media/shared/forensic/SADEDINE-2026/ANALYSES/SD-03/SD03.E01'
ssh -F /home/chris/.ssh/config sift 'sudo -n mmls /mnt/ewf-sd03/ewf1'
ssh -F /home/chris/.ssh/config sift 'sudo -n fsstat -o 8192 /mnt/ewf-sd03/ewf1'
ssh -F /home/chris/.ssh/config sift 'sudo -n fls -o 8192 -r -p /mnt/ewf-sd03/ewf1'
ssh -F /home/chris/.ssh/config sift 'sudo -n istat -z UTC -o 8192 /mnt/ewf-sd03/ewf1 714049800'
ssh -F /home/chris/.ssh/config sift 'sudo -n icat -r -o 8192 /mnt/ewf-sd03/ewf1 1543'
```


## Consultations Freebox et exemples d’authentification

Les anciens exemples d’authentification sont remplacés par la notice paramétrée `freebox/api.md`, sans reprise des secrets. Les endpoints consultés sont conservés dans les fichiers JSON de preuve : LAN `pub`, fiches MAC ciblées, interfaces, Wi-Fi AP/stations, DHCP statique/dynamique, connexion et journaux, port-forwarding, UPnP, DMZ, VPN client, downloads/uploads/feeds et requêtes RRD. Les réponses et codes d’échec restent des sources inchangées ; les commandes anciennes employant une désactivation de contrôle TLS ne sont pas proposées comme méthode courante. L’échantillon MediaInfo du disque Freebox est conservé au bloc 1 ; il porte sur un enregistrement TV et n’authentifie pas un enregistrement de caméra.
