# TP Docker – Optimisation d’une application Node.js

a partir d’un Dockerfile volontairement non optimisé on améliore:
- la taille de l’image
- le temps de build
- la reproductibilité du build
- la sécurité du conteneur

## 2. l’application

L’application fournie est simple :
- un fichier `server.js`
- un serveur Node.js
- écoute sur le port 3000
- affiche un message "Hello World"

## 3. Step0 – baseline Dockerfile non optimisé

Au départ le Dockerfile contient plusieurs mauvaises pratiques :
- image de base `node:latest`
- copie du dossier `node_modules` depuis la machine hôte
- utilisation de `npm install`
- installation de dépendances système inutiles (`apt-get`)
- variable `NODE_ENV=development`
- exécution du conteneur en tant que `root`

### lES problèmes observés:
- l’image est très lourde
- le build dépend de la machine locale
- le cache Docker est mal utilisé
- des dépendances inutiles sont présentes dans l’image finale
- risque de sécurité lié à l’utilisateur `root`

### résultats:
- Image : `tp-node:step0`
- Taille : **1.72 GB** (content size : 433 MB)
- Temps de build : **environ 3.7 secondes**
Cette étape sert de référence pour comparer les optimisations par la suite

## 4. Step1 – nettoyage du build et amélioration du cache
### Modifications apportées

- ajout d’un fichier `.dockerignore`
- suppression de `COPY node_modules`
- copie séparée de `package.json` et `package-lock.json`
- remplacement de `npm install` par `npm ci`

## Explication des commandes

npm ci --> installe les dépendances à partir du fichier `package-lock.json`.
contrairement à `npm install` elle garantit que les mêmes versions seront
installées à chaque build (build reproductible) 
Le fait de copier d’abord `package.json` et `package-lock.json` permet également à Docker de réutiliser le cache si ces fichiers ne changent pas, ce qui accélère les builds suivants.

### Résultats:
- Image : `tp-node:step1`
- Taille : **1.65 GB** (content size : 412 MB)
- Temps de build : **~3.2 s**

## Step2 – Réduction  de la taille de l’image
- passage de `node:latest` à `node:22-alpine`
- passage en mode production
-on installe uniquement les dépendances nécessaires à l’exécution

npm ci --omit=dev  ---> Cette commande installe uniquement les dépendances de production les dépendances de développement ne sont pas nécessaires dans l’image finale et augmentent inutilement sa taille
l’image Alpine est beaucoup plus légère que les images basées sur Debian

## Résultats:
Image : tp-node:step2
taille : 256 MB (content size : 62 MB)
temps de build : ~31 s

## Step3 – Sécurité : exécution en tant que non-root
USER node ---> Par défaut un conteneur Docker s’exécute en tant que root
non-root permet de limiter les risques en cas de faille de sécurité

## Résultats
image : tp-node:step3
Taille : 256 MB (content size : 62 MB)
temps de build : ~4 s