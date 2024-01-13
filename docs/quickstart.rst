Démarrage rapide
================

Localement
----------

Si l'application est disponible localement, 

#. Executez le serveur de développement : *python manage.py runserver*
#. Accédez à l'URL <http://localhost:8000/> dans votre navigateur
#. Pour accéder à l'espace admin, vous devez vous rendre à l'adresse : <http://localhost:8000/admin>  
    - En cas de nouvelle base de données, créez un nouveau super-utilisateur avec la commande : 
    *python manage.py createsuperuser*

Avec Docker
-----------
Une fois l'image Docker obtenu sur votre machine, 
soit en l'ayant *buildé* depuis le code source,
soit en l'ayant *pullé* depuis Docker Hub,
vous pouvez lancer un contenaire ::
    docker run -p 8000:8000 --env-file ./.env.prod <nom-image>:<tag>

En supposant que vos variables d'environnement sans dans le fichier *.env.prod* .

L'application est ensuite accessible localement sur le port 8000.
