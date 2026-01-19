\# TP Docker 



Tous les exercices ont été réalisés en ligne de commande via PowerShell



\## Exercice 1





docker --version cette commande suivante permet d’afficher la version de Docker installée .



docker images Cette commande permet de voir quelles images Docker sont déjà disponibles sur la machine.





\## Exercice 2 



ici nous avons utilisé une image très simple disponible sur Docker Hub : `hello-world`.



Nous avons d’abord téléchargé l’image avec : docker pull hello-world



Puis nous avons exécuté un conteneur basé sur cette image : docker run hello-world



Ce conteneur affiche un message de bienvenue expliquant brièvement

le fonctionnement de Docker.



Nous avons ensuite utilisé :



docker ps  

docker ps -a  



Ces commandes permettent d’afficher les conteneurs en cours d’exécution et l’historique de tous les conteneurs actifs ou arrêtés.



supprimer un conteneur et une image avec :



docker rm <id\_conteneur>  

docker rmi <id\_image>



---



\## Exercice 3 – Création d’un serveur web Nginx



Nous avons commencé par télécharger l’image officielle Nginx :



docker pull nginx



Puis nous avons lancé un conteneur en arrière-plan :



docker run -d -p 8080:80 --name mon\_nginx nginx



cette commande démarre un serveur web accessible depuis un navigateur à l’adresse : http://localhost:8080

vérifié que le conteneur était bien en cours d’exécution avec : docker ps



pour finir arrêté et supprimé le conteneur :



docker stop mon\_nginx  

docker rm mon\_nginx



---



\## Exercice 4 – Déploiement d’une application Flask avec Docker



ici nous avons créé une application web simple en Python

avec Flask puis nous l’avons conteneurisée avec Docker.



Le dossier `tp-flask` contient deux fichiers :

\- `app.py`

\- `Dockerfile`



l’application Flask affiche un message “Hello World from Flask + Docker!”



Le fichier Dockerfile permet de :

\- partir d’une image Python legére

\- copier le fichier `app.py` dans le conteneur

\- installer Flask

\- exposer le port 5000

\- lancer l’application automatiquement au démarrage du conteneur



Nous avons construit l’image avec : docker build -t tp-flask .



Puis lancé le conteneur avec : docker run -d -p 5000:5000 --name mon\_flask tp-flask



l’appli est accessible via : http://localhost:5000



---



\## Exercice 5 – Docker Compose (Flask + MongoDB)



Docker Compose pour lancer plusieurs conteneurs en même temps.



le fichier `docker-compose.yml` pour définir deux services :

\- une application Flask

\- une base de données MongoDB



Docker Compose permet de :

\- lancer plusieurs conteneurs avec une seule commande

\- gérer les dépendances entre services

\- simplifier le déploiement d’applications multi-conteneurs



Le lancement se fait avec : docker compose up





