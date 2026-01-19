# TP Docker Optimisation — Notes de mesure

Contexte : le Dockerfile se trouve dans `./tpdockeroptimisation/`.
Commandes utilisées :
- Build : `docker build -t tp-node:stepX .\tpdockeroptimisation`
- Mesure du temps : `Measure-Command { docker build -t tp-node:stepX .\tpdockeroptimisation }`
- Taille : `docker image ls tp-node:stepX` + `docker history tp-node:stepX`

## Step0 (baseline)

- Image: tp-node:step0
- Taille: 1.72GB (content size 433MB)
- Build time: 3.70s
- Remarques:
  - Base image `node:latest` ( lourde)
  - Copie `node_modules` depuis l’hôte (mauvaise pratique, non portable)
  - `npm install` au lieu de `npm ci` (moins reproductible)
  - `apt-get` + `build-essential` dans l’image finale (gonfle l’image)
  - `NODE_ENV=development` dans l’image finale

## Step1 (.dockerignore + Dockerfile plus cache-friendly)

- Image: tp-node:step1
- Taille: 1.65GB (content size 412MB)
- Build time: 3.17s
- Impact / remarques:
  - Contexte de build réduit grâce à `.dockerignore`
  - Meilleur usage du cache : `COPY package*.json` puis `npm ci`
  - Suppression de `COPY node_modules` (build plus propre et portable)

## Step2 (node:22-alpine + deps prod uniquement)

- Image: tp-node:step2
- Taille: 256MB (content size 62MB)
- Build time: 31.17s
- Remarques:
  - Passage de `node:latest` (Debian) à `node:22-alpine` (beaucoup plus léger)
  - `NODE_ENV=production`
  - `npm ci --omit=dev` : n’installe pas les dépendances de dev
  - Réduction drastique de la taille (1.65GB -> 256MB)
  - Temps de build plus long ici car dépend fortement du téléchargement (pull base + npm) et du cache à ce moment-là

## Step3 (run as non-root)

- Image: tp-node:step3
- Taille: 256MB (content size 62MB)
- Build time: 3.99s
- Remarques:
  - Ajout de `USER node` pour éviter l’exécution en root (bonne pratique sécurité)
  - Aucun impact sur la taille, mais réduit les risques si le conteneur est compromis

## Conclusion

- Gain majeur : réduction de taille ~1.72GB -> 256MB.
- Gain sécurité : exécution en non-root (Step3).
- Builds plus fiables : `npm ci` + meilleure exploitation du cache Docker (Step1/Step2).
