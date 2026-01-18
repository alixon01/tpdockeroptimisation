\## Step0 (baseline)

\- Image: tp-node:step0

\- Taille: 1.72GB (content size 433MB)

\- Build time: 3.70s

\- Remarques:

&nbsp; - Base image node:latest (non pin, lourde)

&nbsp; - Copiait node\_modules depuis l’hôte (mauvaise pratique)

&nbsp; - npm install au lieu de npm ci (moins reproductible)

&nbsp; - apt-get + build-essential dans l’image finale (gonfle l’image)

&nbsp; - NODE\_ENV=development dans l’image finale



\## Step1 (.dockerignore + fix Dockerfile: no COPY node\_modules)

\- Image: tp-node:step1

\- Taille: 1.65GB (content size 412MB)

\- Build time: 3.17s

\- Impact:

&nbsp; - Contexte de build réduit (.dockerignore)

&nbsp; - Meilleur cache Docker (COPY package\*.json puis npm ci)

&nbsp; - Suppression de COPY node\_modules (build plus propre et portable)



