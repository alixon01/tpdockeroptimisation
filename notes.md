## TP Docker Optimisation

le Dockerfile se trouve dans `./tpdockeroptimisation/`.
Commandes utilisées :
- Build : `docker build -t tp-node:stepX .\tpdockeroptimisation`
- Mesure du temps : `Measure-Command { docker build -t tp-node:stepX .\tpdockeroptimisation }`
- Taille : `docker image ls tp-node:stepX` + `docker history tp-node:stepX`

## Step0  
- Image: tp-node:step0
- Taille: 1.72GB (content size 433MB)
- Build time: 3.70s
- Remarques:
  - Base image `node:latest` ( lourde)
  - Copie `node_modules` depuis l’hôte (mauvaise pratique)
  - `npm install` au lieu de `npm ci` (moins reproductible)
  - `apt-get` + `build-essential` dans l’image finale (gonfle l’image)
  - `NODE_ENV=development` dans l’image finale

## Step1 (.dockerignore + Dockerfile plus cache-friendly)

- Image: tp-node:step1
- Taille: 1.65GB (content size 412MB)
- Build time: 3.17s
- remarques:
  - Contexte de build réduit grâce à `.dockerignore`
  - meilleur usage du cache : `COPY package*.json` puis `npm ci`
  - suppression de `COPY node_modules` (build plus propre et portable)

## Step2 (node:22-alpine + deps prod uniquement)

- Image: tp-node:step2
- Taille: 256MB (content size 62MB)
- Build time: 31.17s
- remarques:
  - Passage de `node:latest` (Debian) à `node:22-alpine` (beaucoup plus léger)
  - `NODE_ENV=production`
  - `npm ci --omit=dev` : n’installe pas les dépendances de dev
  - Réduction de la taille (1.65GB -> 256MB)
  - temps de build plus long car dépend du téléchargement (pull base + npm) et du cache à ce moment là

## Step3 (run en non-root)

- Image: tp-node:step3
- taille: 256MB (content size 62MB)
- Build time: 3.99s
ajout de `USER node` pour éviter l’exécution en root //une bonne pratique sécurité

