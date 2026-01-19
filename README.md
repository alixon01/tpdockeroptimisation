# TP Docker – Optimisation d’une application Node.js


À partir d’une application Node.js volontairement non optimisée, plusieurs étapes d’amélioration sont réalisées afin de :
- réduire la taille de l’image
- améliorer le temps de build
- rendre le build reproductible
- renforcer la sécurité du conteneur

## 2. Description de l’application

L’application est un serveur Node.js très simple :
- fichier principal : `server.js`
- serveur HTTP écoutant sur le port 3000
- réponse affichée :
--> Hello world — serveur volontairement non optimisé mais fonctionnel

## 3. Step0 – Baseline (image non optimisée)
### Dockerfile (principe)
- Image de base : `node:latest`
- Copie du dossier `node_modules` depuis la machine hôte
- Utilisation de `npm install`
- Installation de dépendances système via `apt-get`
- Exécution en tant que `root`
- Variable `NODE_ENV=development`

### Problèmes identifiés
- Image très lourde
- Build non reproductible
- Mauvaise gestion du cache Docker
- Risques de sécurité (root)
- Dépendances inutiles dans l’image finale
### Résultats
- Image : `tp-node:step0`
- Taille : **1.72 GB** (content size : 433 MB)
- Temps de build : **~3.7 s**

## Step1 – Nettoyage du build et cache Docker

### Optimisations réalisées
- Ajout d’un fichier `.dockerignore`
- Suppression de `COPY node_modules`
- Copie séparée des fichiers `package.json` et `package-lock.json`
- Utilisation de `npm ci` (installation reproductible)


Le cache Docker est mieux exploité
Le build devient portable (indépendant de la machine hôte)
Le contexte de build est réduit

### Résultats
- Image : `tp-node:step1`
- Taille : **1.65 GB** (content size : 412 MB)
- Temps de build : **~3.2 s**

## 5. Step2 – Réduction drastique de la taille
Réduire fortement la taille de l’image finale.

### Optimisations réalisées
- Passage de `node:latest` (Debian) à `node:22-alpine`
- Définition de `NODE_ENV=production`
- Installation uniquement des dépendances de production :
  ```bash
  npm ci --omit=dev
