# candi-app
Interface pour candidature



# Deployment:

La version en prodcution utilise Postgre sql. Attention la dernière version de SQLAlchemy n'est pas compatible avec heroku, il faut utiliser la version dans les requirements.
Après avoir push sur heroku, il faut accèder à la console du serveur et initialiser la db: python create.py
