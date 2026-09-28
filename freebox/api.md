# Connexion à l'api de la freebox

## Variables préalables

```bash
APP_TOKEN='Ocs6IU76SZgJTjGw2dGjpqzOe15y4TQrdICciCdB+AB8qc60gERrflVb6sde/Gki'
APP_ID='fr.donnat.freebox.forensic'
BASE_URL='https://v28vy0w8.fbxos.fr:9717/api/v16'
```

## Vérifier qu'une session est déjà ouverte

Pour vérifier:

```bash
curl -sk "$BASE_URL/system/" \
  -H "X-Fbx-App-Auth: $SESSION_TOKEN" | jq
```

On doit obtenir: `"success": "true"`

## Obtenir un session_token

Pour obtention du session_token, la requête POST suivante a été effectuée sur l’endpoint `/login/session` :

```bash
CHALLENGE=$(curl -sk "$BASE_URL/login/" | jq -r '.result.challenge')

PASSWORD=$(printf '%s' "$CHALLENGE" | openssl dgst -sha1 -hmac "$APP_TOKEN" | awk '{print $NF}')

SESSION_JSON=$(curl -sk -X POST "$BASE_URL/login/session/" \
  -H 'Content-Type: application/json' \
  -d "{\"app_id\":\"$APP_ID\",\"app_version\":\"1.0\",\"password\":\"$PASSWORD\"}")

echo "$SESSION_JSON" | jq

SESSION_TOKEN=$(printf '%s' "$SESSION_JSON" | jq -r '.result.session_token')
```




