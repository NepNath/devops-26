# Bonus image moins de 500 Bytes

Objectif : creer l'image Docker la plus petite possible capable d'afficher les nombres de `0` a `10000`.

Une image strictement inferieure a 500 Bytes est un challenge extreme et depend de la facon dont la taille est mesuree. Le Dockerfile classique ci-dessous ne passera generalement pas sous 500 Bytes avec les metadonnees Docker, mais il donne une base tres compacte avec une image `scratch`.

Build :

```bash
docker build -t wik-dps-bonus:tiny .
```

Run :

```bash
docker run --rm wik-dps-bonus:tiny
```

Verifier la taille :

```bash
docker image ls wik-dps-bonus:tiny
```
