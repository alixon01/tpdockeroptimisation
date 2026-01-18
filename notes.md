\## Step0 (baseline)

\- Image: tp-node:step0

\- Taille:1.72GB (content size 433MB)

\- Build time:3.70s

\- Remarques:

FROM node:latest (non pin + lourd)



COPY node\_modules (mauvaise pratique)



npm install (moins reproductible que npm ci)



apt-get install build-essential dans l’image finale (gonfle l’image)



NODE\_ENV=development (pas prod)

