# Obtenir un track_id

## Sur la machine en local

```powershell
$body=@{app_id="fr.donnat.freebox.forensic";app_name="Analyse Freebox - Christophe Donnat";app_version="1.0";device_name="PC Mme Sadedine"}|ConvertTo-Json;$response=Invoke-RestMethod -Method POST -Uri "http://mafreebox.freebox.fr/api/v16/login/authorize/" -ContentType "application/json" -Body $body;$response.result
```

Vérifier

```powershell
curl.exe "http://mafreebox.freebox.fr/api/v16/login/authorize/2{track_id}"
```

On doit obtenir: `"status": "granted"`

## Sur la machine distante

Remplacer la valeur de APP_TOKEN par la valeur obtenue:

```bash
APP_TOKEN='{APP_TOKEN}'
APP_ID='fr.donnat.freebox.forensic'
BASE_URL='https://v28vy0w8.fbxos.fr:9717/api/v16'

CHALLENGE=$(curl -sk "$BASE_URL/login/" | jq -r '.result.challenge')

PASSWORD=$(printf '%s' "$CHALLENGE" | openssl dgst -sha1 -hmac "$APP_TOKEN" | awk '{print $NF}')

SESSION_JSON=$(curl -sk -X POST "$BASE_URL/login/session/" \
  -H 'Content-Type: application/json' \
  -d "{\"app_id\":\"$APP_ID\",\"app_version\":\"1.0\",\"password\":\"$PASSWORD\"}")

echo "$SESSION_JSON" | jq

SESSION_TOKEN=$(printf '%s' "$SESSION_JSON" | jq -r '.result.session_token')

curl -sk "$BASE_URL/system/" \
  -H "X-Fbx-App-Auth: $SESSION_TOKEN" | jq
```

On doit obtenir: `"success": "true"`


---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---































```powershell
curl.exe http://mafreebox.freebox.fr/api_version


curl.exe -X POST `
  http://mafreebox.freebox.fr/api/v16/login/authorize/ `
  -H "Content-Type: application/json" `
  -d "{\"app_id\":\"fr.donnat.freebox.forensic\",\"app_name\":\"Analyse Freebox - Christophe Donnat\",\"app_version\":\"1.0\",\"device_name\":\"PC Mme Sadedine\"}"

```

## Réponse:
"app_token": "..."
"track_id": ...

Tester mon ordi:

```powershell
curl.exe `
  http://mafreebox.freebox.fr/api/v16/login/authorize/[track_id]`
  ```


  ---


  Oui. Une fois que l’application a déjà été autorisée sur la Freebox et que tu possèdes ton `app_token`, voilà la procédure exacte pour ouvrir une session API depuis ta machine.

Freebox OS fonctionne en 3 étapes : récupérer le `challenge`, calculer le HMAC-SHA1 avec l’`app_token`, puis demander un `session_token`. C’est bien le mécanisme encore utilisé avec l’API v16. ([Freebox Dev][1])

### 1. Définir ton `APP_ID` et ton `APP_TOKEN`

Sur ton Mac/Linux :

```bash
APP_ID='fr.donnat.freebox.forensic'
APP_TOKEN='TON_APP_TOKEN_ICI'
```

Ne mets pas le vrai `APP_TOKEN` dans un rapport ou un historique partagé : il doit rester secret.

### 2. Récupérer le `challenge`

Tu interroges :

```bash
curl -sk \
  'https://mafreebox.freebox.fr/api/v16/login/'
```

Tu dois recevoir quelque chose de ce type :

```json
{
  "success": true,
  "result": {
    "logged_in": false,
    "challenge": "xxxxxxxxxxxxxxxxxxxxxxxx",
    "password_salt": "xxxxxxxx"
  }
}
```

La valeur qui nous intéresse est :

```text
challenge
```

Tu peux l’extraire automatiquement si tu as `jq` :

```bash
CHALLENGE=$(curl -sk \
  'https://mafreebox.freebox.fr/api/v16/login/' \
  | jq -r '.result.challenge')
```

Vérifie :

```bash
echo "$CHALLENGE"
```

### 3. Calculer le `password`

La formule correcte est :

```text
HMAC-SHA1(
    message = challenge,
    key = app_token
)
```

Autrement dit, **l’`app_token` est la clé HMAC** et le `challenge` est le message. C’est notamment la forme confirmée dans les exemples Freebox : `hash_hmac("sha1", $challenge, $app_token)`. ([Freebox Dev][2])

Avec OpenSSL :

```bash
PASSWORD=$(printf '%s' "$CHALLENGE" \
  | openssl dgst -sha1 -hmac "$APP_TOKEN" \
  | sed 's/^.*= //')
```

Puis :

```bash
echo "$PASSWORD"
```

Tu obtiendras une chaîne hexadécimale, par exemple :

```text
7d2895e73ec42b13be81031741e358....
```

### 4. Demander le `session_token`

Maintenant :

```bash
curl -sk \
  -X POST \
  'https://mafreebox.freebox.fr/api/v16/login/session/' \
  -H 'Content-Type: application/json' \
  -d "{
    \"app_id\":\"$APP_ID\",
    \"password\":\"$PASSWORD\"
  }"
```

Si tout va bien, tu obtiens quelque chose comme :

```json
{
  "success": true,
  "result": {
    "session_token": "xxxxxxxxxxxxxxxxxxxxxxxx",
    "challenge": "xxxxxxxx",
    "permissions": {
      ...
    }
  }
}
```

Récupère automatiquement le token :

```bash
SESSION_TOKEN=$(curl -sk \
  -X POST \
  'https://mafreebox.freebox.fr/api/v16/login/session/' \
  -H 'Content-Type: application/json' \
  -d "{
    \"app_id\":\"$APP_ID\",
    \"password\":\"$PASSWORD\"
  }" \
  | jq -r '.result.session_token')
```

Puis :

```bash
echo "$SESSION_TOKEN"
```

### 5. Tester que la session fonctionne

Par exemple avec l’endpoint système :

```bash
curl -sk \
  'https://mafreebox.freebox.fr/api/v16/system/' \
  -H "X-Fbx-App-Auth: $SESSION_TOKEN"
```

Ou pour tester les équipements du LAN :

```bash
curl -sk \
  'https://mafreebox.freebox.fr/api/v16/lan/browser/pub/' \
  -H "X-Fbx-App-Auth: $SESSION_TOKEN"
```

Les appels authentifiés utilisent bien :

```http
X-Fbx-App-Auth: <session_token>
```

y compris sur les API v16 actuelles. ([Freebox Dev][3])

### Version complète à copier-coller

Si `jq` et `openssl` sont installés :

```bash
APP_ID='fr.donnat.freebox.forensic'
APP_TOKEN='TON_APP_TOKEN_ICI'

CHALLENGE=$(curl -sk \
  'https://mafreebox.freebox.fr/api/v16/login/' \
  | jq -r '.result.challenge')

echo "Challenge : $CHALLENGE"

PASSWORD=$(printf '%s' "$CHALLENGE" \
  | openssl dgst -sha1 -hmac "$APP_TOKEN" \
  | sed 's/^.*= //')

echo "Password HMAC : $PASSWORD"

SESSION_TOKEN=$(curl -sk \
  -X POST \
  'https://mafreebox.freebox.fr/api/v16/login/session/' \
  -H 'Content-Type: application/json' \
  -d "{
    \"app_id\":\"$APP_ID\",
    \"password\":\"$PASSWORD\"
  }" \
  | jq -r '.result.session_token')

echo "Session token : $SESSION_TOKEN"

curl -sk \
  'https://mafreebox.freebox.fr/api/v16/system/' \
  -H "X-Fbx-App-Auth: $SESSION_TOKEN" \
  | jq
```

Le point auquel il faut faire attention dans **ton cas précis**, c’est l’adresse :

```text
https://mafreebox.freebox.fr
```

Ces commandes sont parfaites lorsque tu es **sur le LAN de la Freebox concernée**. Depuis chez toi pour atteindre **la Freebox de Mme Sadedine**, il faudra remplacer cette base URL par son **adresse d’accès distant HTTPS + son port**, par exemple quelque chose de la forme :

```text
https://xxxxxxxx.freeboxos.fr:12345
```

Ensuite, exactement la même séquence `login → challenge → HMAC → login/session → X-Fbx-App-Auth` s’applique.

Si tu veux, on peut maintenant faire **la procédure spécifique accès distant**, étape par étape, pour que tu puisses ouvrir cette session depuis ton Mac sans être physiquement chez Mme Sadedine.

[1]: https://dev.freebox.fr/bugs/task/39911?utm_source=chatgpt.com "FS#39911 : Freebox API Login Track \"/api/v8/login/authorize/\""
[2]: https://dev.freebox.fr/bugs/task/36981?order=category&p_____x=&pagenum=64&sort=desc&utm_source=chatgpt.com "FS#36981 : [résolu] 2022, API mafreebox.freebox.fr, session token, erreur dans la Doc"
[3]: https://dev.freebox.fr/bugs/task/41161?utm_source=chatgpt.com "FS#41161 : Freebox Ultra V9 : échecs intermittents du handshake WPA/EAPOL avec une Nest Cam 3e génération"
