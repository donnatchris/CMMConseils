# Reproduire les consultations Freebox OS / API

Cette notice réunit les parcours locaux PowerShell et distants Bash auparavant séparés. Elle décrit une méthode ; aucune nouvelle consultation de la Freebox n’est exécutée par la révision documentaire du 18 novembre 2026. Les réponses de référence sont sous `preuves-json/` ; l’API utilisée lors de la collecte était v16. Les paramètres et secrets se renseignent séparément et ne font partie ni de la livraison ni des exemples.

## Prérequis et autorisation initiale

Disposer de l’autorisation du titulaire, de l’adresse HTTPS et du port de la Freebox, d’un identifiant d’application et de la version API annoncée par l’appareil. L’association initiale modifie les autorisations : elle nécessite la validation physique sur le Server. Elle reste distincte des consultations GET ultérieures.

Sous PowerShell, avec les valeurs renseignées dans les variables, envoyer la demande d’association :

```powershell
$BaseUrl = Read-Host 'Base HTTPS incluant /api/v16'
$AppId = Read-Host 'Identifiant application'
$Body = @{app_id=$AppId; app_name='Analyse autorisée'; app_version='1.0'; device_name='Poste d’analyse'} | ConvertTo-Json
$Association = Invoke-RestMethod -Method Post -Uri "$BaseUrl/login/authorize/" -ContentType 'application/json' -Body $Body
$TrackId = $Association.result.track_id
Invoke-RestMethod -Method Get -Uri "$BaseUrl/login/authorize/$TrackId"
```

Attendre le statut `granted` après validation physique. Le `app_token` renvoyé est un secret à conserver dans le moyen séparé prévu pour les accès ; ne pas exporter la réponse d’association dans le dossier de rapports. Une association de mission ne prouve aucun accès ancien.

## Consultation avec une application déjà associée

La session utilise un challenge fourni par `GET login/`, puis un HMAC-SHA1 du challenge avec `app_token` pour `POST login/session/`. Le jeton de session reste en mémoire et passe dans `X-Fbx-App-Auth`. Le script [consulter-freebox.py](consulter-freebox.py) exécute ce parcours sans inclure les secrets dans les arguments ou journaux :

```bash
python3 freebox/consulter-freebox.py --base-url 'https://ADRESSE:PORT/api/v16' --app-id 'IDENTIFIANT_APPLICATION' --out /tmp/freebox-controle-nouveau
```

Le script demande le secret sans écho, crée une destination nouvelle et n’exécute que les GET `system/` et `lan/browser/pub/` une fois la session ouverte. Il enregistre les réponses de ces consultations et leurs SHA-256, puis ferme la session. Les autres endpoints de référence sont décrits dans le rapport et les réponses conservées : Wi-Fi, DHCP, connexion, DMZ, redirections, VPN, transferts et statistiques. Une extension de collecte doit conserver endpoint exact, paramètres, UTC, réponse et code d’erreur ; une erreur de statistiques n’est pas un volume nul.

## Résultats attendus et limites

Les requêtes réussies renvoient `success: true`. Le relevé de référence comporte 74 fiches LAN, dont 56 avec une trace antérieure au 29 octobre 2024 ; une consultation actuelle n’a pas à retrouver exactement ces nombres, puisque la Freebox évolue. Les dates premières/dernières mémorisées ne constituent pas un journal continu ni une preuve d’utilisation par une personne. Le [rapport Freebox](analyse-freebox.md) explique les champs et les limites des adresses privées. Aucun secret des anciens exemples n’est repris ici.

---

Révision documentaire : 18 novembre 2026. Les dates des faits et des analyses restent celles indiquées dans le texte.

Christophe DOnnat — Donnat Dev
