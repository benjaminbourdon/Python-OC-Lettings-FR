Déploiement
===========

Pipeline Circle CICD
--------------------

Pour son bon fonctionnement, la pipeline CICD configurée sous CircleCI nécessite de
connaître les informations liées aux services Docker Hub et AWS.
En particulier, l'accès AWS utilisé doit avoir accès au service *Elastic Container Registry*.
Pour cela, la création d'un contexte nommé **aws** au sein de votre organisation sur Circle CI.

Enfin, voici les variables d'environnement à fournir sur CircleCI :
Ces variables peuvent être définies au niveau du prochain ou encore du contexte selon votre usage.

.. csv-table:: Variables d'environnement
   :header: "Nom", "Description"
   :widths: 15, 15

    "AWS_ACCESS_KEY_ID",    "Clé d'identification AWS"
    "AWS_ACCOUNT_ID",   "Numéro d'identification du compte AWS"
    "AWS_DEFAULT_REGION",   "Région utilisée par défaut par le compte AWS"
    "AWS_SECRET_ACCESS_KEY",    "Clé secrète d'accès AWS"
    "DOCKER_PASSWORD",  "Mot de passe Docker Hub"
    "DOCKER_USERNAME",  "Nom d'utilisateur Docker Hub"

Amazon Elastic Container Registry (ECR)
---------------------------------------

Le déploiement repose sur la création d'une image de l'application sur AWS ECR.
Cette image peut ensuite être utilisée pour la mise en ligne via le service App Runner d'AWS.

Il vous faut donc définir les variables d'environnement suivantes au sein d'App Runner :

.. csv-table:: Variables d'environnement
   :header: "Nom", "Description"
   :widths: 15, 15

   "DJANGO_ALLOWED_HOSTS",	"Valeur de la variable du même nom de Django."
   "SENTRY_DSN",	"Clé API de Sentry"
   "SECRET_KEY",	"Clé secrète du setup Django"