#!/usr/bin/env bash
set -Eeuo pipefail

IMAGE='/media/shared/forensic/SADEDINE-2026/OP-01/OP01.E01'
EWF_MOUNT='/mnt/ewf'
DISLOCKER_MOUNT='/mnt/dislocker'
WINDOWS_MOUNT='/mnt/windows'

if (( EUID != 0 )); then
  exec sudo bash "$0" "$@"
fi

for command in ewfmount losetup dislocker ntfs-3g findmnt lsblk; do
  command -v "$command" >/dev/null || { echo "Commande absente : $command" >&2; exit 1; }
done

[[ -f "$IMAGE" ]] || { echo "Image absente : $IMAGE" >&2; echo 'Vérifie le montage du dossier partagé /media/shared.' >&2; exit 1; }
mkdir -p "$EWF_MOUNT" "$DISLOCKER_MOUNT" "$WINDOWS_MOUNT"

if findmnt -rn --mountpoint "$WINDOWS_MOUNT" >/dev/null; then
  echo "Déjà monté : $WINDOWS_MOUNT"
  findmnt "$WINDOWS_MOUNT"
  exit 0
fi

if ! findmnt -rn --mountpoint "$EWF_MOUNT" >/dev/null; then
  echo '[1/4] Montage EWF'
  ewfmount "$IMAGE" "$EWF_MOUNT"
else
  echo '[1/4] Montage EWF déjà présent'
fi

EWF_FILE="$EWF_MOUNT/ewf1"
[[ -e "$EWF_FILE" ]] || { echo "Vue EWF absente : $EWF_FILE" >&2; exit 1; }

# Réutiliser le loop créé lors d'un éventuel lancement précédent.
LOOP_DEVICE=''
while IFS= read -r line; do
  candidate="${line%% *}"
  if [[ "$line" == *"$EWF_FILE"* ]]; then
    LOOP_DEVICE="$candidate"
    break
  fi
done < <(losetup -l -n -O NAME,BACK-FILE 2>/dev/null)

if [[ -z "$LOOP_DEVICE" ]]; then
  echo '[2/4] Création loop en lecture seule'
  LOOP_DEVICE="$(losetup --find --partscan --read-only --show "$EWF_FILE")"
else
  echo "[2/4] Loop existant : $LOOP_DEVICE"
  [[ "$(lsblk -dn -o RO "$LOOP_DEVICE" | tr -d ' ')" == '1' ]] || { echo 'ERREUR : loop existant pas en lecture seule' >&2; exit 1; }
  partprobe "$LOOP_DEVICE" 2>/dev/null || true
fi

command -v udevadm >/dev/null && udevadm settle
PARTITION="${LOOP_DEVICE}p3"
if [[ ! -b "$PARTITION" ]]; then
  echo "Partition attendue absente : $PARTITION" >&2
  lsblk "$LOOP_DEVICE" >&2
  exit 1
fi

echo "Source : $PARTITION"
[[ "$(lsblk -dn -o RO "$LOOP_DEVICE" | tr -d ' ')" == '1' ]] || { echo 'ERREUR : loop pas en lecture seule' >&2; exit 1; }

if [[ -f "$DISLOCKER_MOUNT/dislocker-file" ]] && findmnt -rn --mountpoint "$DISLOCKER_MOUNT" >/dev/null; then
  echo '[3/4] BitLocker déjà déverrouillé'
else
  if findmnt -rn --mountpoint "$DISLOCKER_MOUNT" >/dev/null; then
    echo "Montage Dislocker présent, mais dislocker-file absent. Vérifie manuellement $DISLOCKER_MOUNT." >&2
    exit 1
  fi
  echo '[3/4] Déverrouillage BitLocker (saisir la clé de récupération au prompt)'
  dislocker -r -V "$PARTITION" -p -- "$DISLOCKER_MOUNT"
fi

[[ -f "$DISLOCKER_MOUNT/dislocker-file" ]] || { echo 'Dislocker-file absent après déverrouillage' >&2; exit 1; }

echo '[4/4] Montage NTFS en lecture seule, sans rejeu du journal'
ntfs-3g -o ro,norecover "$DISLOCKER_MOUNT/dislocker-file" "$WINDOWS_MOUNT"

echo
echo 'Montage terminé :'
findmnt "$WINDOWS_MOUNT"
lsblk -o NAME,SIZE,FSTYPE,RO,TYPE,MOUNTPOINT "$LOOP_DEVICE"
[[ -f "$WINDOWS_MOUNT/Windows/System32/winevt/Logs/System.evtx" ]] && echo 'OK : System.evtx accessible'
echo "Accès : $WINDOWS_MOUNT"
