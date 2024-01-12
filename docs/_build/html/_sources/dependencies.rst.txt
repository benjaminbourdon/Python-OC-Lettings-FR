Dépendances
===========

Au delà de Python version 3.6 ou supérieure, le site s'appuie sur :

- **Django** : framework servant le site 
- **python-dotenv** pour les variables d'environnement
- **sentry-sdk** : pour la journalisation des logs
- **whitenoise** : pour la gestion des fichiers static en production

Le site utilise également **flake8** pour le linting et **pytest** pour le testing.

Pour la production, la pipeline CICD repose sur **CircleCI** et **GitHub**.
Le site est hébergé via AWS.

La documentation est fournie par **sphinx** et **Readthedocs**.