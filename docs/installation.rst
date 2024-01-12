Installation
<<<<<<< HEAD
============
=======
============

Prérequis
---------

- Compte GitHub avec accès en lecture au repository du projet
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Variables d'environnement
-------------------------


Installation locale
-------------------

#. Clonez ce dépôt sur votre machine locale :
    git clone https://github.com/benjaminbourdon/Python-OC-Lettings-FR.git
#. Accédez au répertoire du projet. 
#. Créez un environnement virtuel.  
    La documentation recommande *pipenv*. 
    Si *pipenv* est déjà installé sur votre système :: 
        pipenv install 
    Alternativement, avec *venv* ::
        python3 -m venv env
#. Activez l'environnement virtuel :
    + Avec *pipenv* : *pipenv shell*
    + Avec *venv* : 
        + Sur macOS et Linux : *source env/bin/activate*
        + Sur Windows avec PowerShell : *env\Scripts\Activate.ps1*

#. Si vous avez choisi *venv*, installez les dépendances manuellement ::
        pip install -r requirements.txt  
    Avec pipenv, les dépendances ont automatiquement été installées lors de la création de l'environnement virtuel. 
    Vous pouvez le vérifier avec : *pipenv graph*
#. Effectuez les migrations de la base de données.  
    Le dépôt inclut un fichier *db.sqlite3* à des fins de test.
    Il est recommandé de supprimer ce fichier et de créer la base de données (vide) avec ::
        python manage.py migrate
#. Lancez le serveur de développement :
    python manage.py runserver

Installation avec Docker
------------------------

Alternativement, une configuration Docker est disponible.
Vous pouvez notamment utiliser ::
    docker-compose build
Vos variables d'environnement doivent alors être disponible dans un fichier *.env.prod*.
Ou alternativement::
    docker build -t <nom-image>:<tag> .
Enfin, la pipeline CICD du projet crée un docker que vous pouvez *pull* depuis Docker Hub.
>>>>>>> Developpement
