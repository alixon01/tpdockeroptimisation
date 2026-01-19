\## Step0 (baseline)

\- Image: tp-node:step0

\- Taille: 1.72GB (content size 433MB)

\- Build time: 3.70s

\- Remarques:

  - Base image node:latest (non pin, lourde)

  - Copiait node\_modules depuis l’hôte (mauvaise pratique)

  - npm install au lieu de npm ci (moins reproductible)

  - apt-get + build-essential dans l’image finale (gonfle l’image)

  - NODE\_ENV=development dans l’image finale



\## Step1 (.dockerignore + fix Dockerfile: no COPY node\_modules)

\- Image: tp-node:step1

\- Taille: 1.65GB (content size 412MB)

\- Build time: 3.17s

\- Impact:

  - Contexte de build réduit (.dockerignore)

  - Meilleur cache Docker (COPY package\*.json puis npm ci)

  - Suppression de COPY node\_modules (build plus propre et portable)



\## Step2 (node:22-alpine + deps prod)

\- Image: tp-node:step2

\- Taille: 256MB (content size 62MB)

\- Build time: 31.17s

\- Remarques:

  - Passage de node:latest (Debian) à node:22-alpine (beaucoup plus léger)

  - NODE\_ENV=production

  - npm ci --omit=dev : n’installe pas les dépendances de dev

  - Image finale drastiquement réduite (1.65GB -> 256MB)



\## Step3 (run as non-root)

\- Image: tp-node:step3

\- Taille: 256MB (content size 62MB)

\- Build time: 3.99s

\- Remarques:

&nbsp; - Ajout de `USER node` pour éviter l’exécution en root (bonne pratique sécurité)

&nbsp; - Aucun impact sur la taille, mais réduit les risques si le conteneur est compromis



