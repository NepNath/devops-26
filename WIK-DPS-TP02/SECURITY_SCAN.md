# Scan de vulnerabilites

Docker n'etait pas accessible dans l'environnement de preparation. Les commandes ci-dessous sont a executer localement apres avoir lance Docker Desktop.

## Image single-stage

```bash
docker build -f Dockerfile.single -t wik-dps-tp02-api:single .
trivy image wik-dps-tp02-api:single
```

Ou avec Docker Scout :

```bash
docker scout cves wik-dps-tp02-api:single
```

## Image multi-stage

```bash
docker build -t wik-dps-tp02-api:multi .
trivy image wik-dps-tp02-api:multi
```

Ou avec Docker Scout :

```bash
docker scout cves wik-dps-tp02-api:multi
```

## Resultats a renseigner

Coller ici les resultats du scanner avant de rendre le depot GitHub.

### `wik-dps-tp02-api:single`

```text
A COMPLETER
```

### `wik-dps-tp02-api:multi`

```text
A COMPLETER
```
