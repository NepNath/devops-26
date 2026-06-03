# ping-api

Serveur HTTP minimal qui renvoie en JSON les headers de la requête sur `GET /ping`.

- **Aucune dépendance externe** — uniquement la bibliothèque standard Python.
- Toute autre route ou méthode HTTP renvoie une réponse vide avec le code `404`.

## Prérequis

- Python 3.8 ou supérieur

## Lancement

```bash
python main.py
```

Par défaut, le serveur écoute sur le port **8080**.

### Port personnalisé

Le port d'écoute est configurable via la variable d'environnement `PING_LISTEN_PORT` :

```bash
# Linux / macOS
PING_LISTEN_PORT=3000 python main.py

# Windows (PowerShell)
$env:PING_LISTEN_PORT=3000; python main.py

# Windows (cmd)
set PING_LISTEN_PORT=3000 && python main.py
```

## Endpoints

| Méthode | Chemin  | Réponse                                              |
|---------|---------|------------------------------------------------------|
| `GET`   | `/ping` | `200 OK` — JSON contenant les headers de la requête  |
| *autre* | *autre* | `404 Not Found` — corps vide                         |

## Exemple

```bash
curl -i http://localhost:8080/ping
```

```
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 70

{"Host": "localhost:8080", "User-Agent": "curl/8.4.0", "Accept": "*/*"}
```