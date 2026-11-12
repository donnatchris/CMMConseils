from pathlib import Path
from getpass import getpass
from iphone_backup_decrypt import EncryptedBackup

BACKUP = Path(
    "/mnt/data/forensic/SADEDINE-2026/TP-02/"
    "00008110-001C69A002BA801E"
)

OUTPUT = Path(
    "/mnt/data/forensic/SADEDINE-2026/"
    "ANALYSES/TP-02/Manifest-decrypted.db"
)

OUTPUT.parent.mkdir(parents=True, exist_ok=True)

password = getpass("Mot de passe sauvegarde iPhone : ")

backup = EncryptedBackup(
    backup_directory=str(BACKUP),
    passphrase=password
)

backup.test_decryption()
backup.save_manifest_file(str(OUTPUT))

print("Déchiffrement réussi.")
print("Fichier :", OUTPUT)