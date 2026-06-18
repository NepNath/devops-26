# WIK-DPS-TP02

Rendu de la consigne 1 : creation d'images Docker pour l'API du TP WIK-DPS-TP01.

## Contenu

- `Dockerfile.single` : image en un seul stage.
- `Dockerfile` : image multi-stage avec un stage de build et un stage d'execution sans les sources.
- `src/server.js` : route `GET /ping`.
- `SECURITY_SCAN.md` : commandes et emplacement pour renseigner les vulnerabilites detectees.
- `bonus/` : base pour le bonus de l'image la plus petite possible.

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

## Image Docker en un seul stage

Build :

```bash
docker build -f Dockerfile.single -t wik-dps-tp02-api:single .
```

Run :

```bash
docker run --rm -p 3000:3000 wik-dps-tp02-api:single
```

Scan avec Trivy :

```bash
mkdir -p scan-results
trivy image wik-dps-tp02-api:single > scan-results/trivy-single.txt
```

Alternative avec Docker Scout :

```bash
docker scout cves wik-dps-tp02-api:single > scan-results/docker-scout-single.txt
```

## Image Docker multi-stage

Build :

```bash
docker build -t wik-dps-tp02-api:multi .
```

Run :

```bash
docker run --rm -p 3000:3000 wik-dps-tp02-api:multi
```

Scan avec Trivy :

```bash
mkdir -p scan-results
trivy image wik-dps-tp02-api:multi > scan-results/trivy-multi.txt
```

Alternative avec Docker Scout :

```bash
docker scout cves wik-dps-tp02-api:multi > scan-results/docker-scout-multi.txt
```

## Publication GitHub

Le repository doit s'appeler `WIK-DPS-TP02`.

Exemple :

```bash
git init
git add .
git commit -m "Add Docker TP02"
git branch -M main
git remote add origin git@github.com:VOTRE_COMPTE/WIK-DPS-TP02.git
git push -u origin main
```

## Notes sur l'optimisation des layers

Les fichiers `package.json` et `package-lock.json` sont copies avant le code source. Docker peut donc reutiliser le cache de `npm ci` quand seul le code de l'API change.

L'image multi-stage ne copie que `dist/` dans l'image d'execution. Les sources restent dans le stage de build.
