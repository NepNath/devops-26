# WIK-DPS-TP03

Rendu de la consigne 2 : Docker Compose avec 4 replicas de l'API et un reverse-proxy nginx expose sur le port `8080`.

## Contenu

- `Dockerfile` : image multi-stage basee sur le Dockerfile du TP02.
- `docker-compose.yaml` : API repliquee 4 fois + reverse-proxy nginx expose sur le port `8080`.
- `nginx/nginx.conf` : load balancing vers le service `api`.
- `src/server.js` : route `GET /ping` qui log le hostname du container.

## Lancer l'API en local

```bash
npm install
npm run build
npm start
```

Puis tester :

```bash
curl http://localhost:3000/ping
```

## Image Docker utilisee par Compose

Build :

```bash
docker build -t wik-dps-tp03-api:multi .
```

Run :

```bash
docker run --rm -p 3000:3000 wik-dps-tp03-api:multi
```

## Docker Compose avec nginx

Lancer les 4 replicas de l'API et nginx :

```bash
docker compose up --build --scale api=4
```

Tester via le reverse-proxy expose sur l'hote :

```bash
curl http://localhost:8080/ping
```

Observer le load balancing :

```bash
docker compose logs -f api
```

Chaque requete `/ping` affiche dans les logs le hostname du container qui a traite la requete.

## Publication GitHub

Le repository peut s'appeler `WIK-DPS-TP03` pour separer ce rendu du TP02.

Exemple :

```bash
git init
git add .
git commit -m "Add Docker Compose TP03"
git branch -M main
git remote add origin git@github.com:VOTRE_COMPTE/WIK-DPS-TP03.git
git push -u origin main
```

## Notes

Les fichiers `package.json` et `package-lock.json` sont copies avant le code source. Docker peut donc reutiliser le cache de `npm ci` quand seul le code de l'API change.

L'image multi-stage ne copie que `dist/` dans l'image d'execution. Les sources restent dans le stage de build, comme dans le TP02.
