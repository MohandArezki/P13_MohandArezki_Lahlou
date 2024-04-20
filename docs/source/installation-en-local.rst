Installation du projet sur votre machine
========================================

Cloner le dépôt
---------------

Pour commencer, créez un dossier pour le projet et accédez-y :

.. code-block:: shell

   mkdir oc_lettings
   cd oc_lettings

Clonez le dépôt dans le dossier courant :

.. code-block:: shell

   git clone https://github.com/MohandArezki/P13_MohandArezki_Lahlou.git .

Créer l'environnement virtuel
-----------------------------

Créez un environnement virtuel Python pour isoler les dépendances du projet :

.. code-block:: shell

   python -m venv venv

Activer l'environnement virtuel
-------------------------------

Activez l'environnement virtuel nouvellement créé :

.. code-block:: shell

   source venv/bin/activate

Installer les prérequis
-----------------------

Installez les dépendances nécessaires au projet à partir du fichier ``requirements.txt`` :

.. code-block:: shell

   pip install -r requirements.txt

Mettre à jour le fichier .env
-----------------------------

Pour configurer l'environnement, mettez à jour le fichier de configuration ``.env`` avec les valeurs appropriées :
    
    OC_LETTINGS_DEBUG : Cette variable détermine si Django fonctionne en mode débogage. Lorsqu'elle est définie sur "True", Django fonctionne en mode débogage, ce qui fournit des messages d'erreur utiles et d'autres informations de débogage. En production, elle devrait être définie sur "False" pour des raisons de sécurité.

    OC_LETTINGS_DJANGO_SECRET_KEY : Il s'agit de la clé secrète utilisée par Django pour la signature cryptographique. Elle est utilisée pour générer des hachages uniques pour les sessions, les jetons CSRF et d'autres fonctionnalités liées à la sécurité. Elle doit être gardée secrète et non partagée publiquement.

    OC_LETTINGS_ALLOWED_HOSTS : Cette variable spécifie une liste séparée par des virgules de noms d'hôtes/domaines que Django peut servir. Elle aide à prévenir les attaques de l'en-tête HTTP Host en permettant à Django de valider l'en-tête Host des requêtes entrantes par rapport à une liste d'hôtes autorisés. Chaque nom d'hôte/domaine doit être ajouté à cette liste.

    OC_LETTINGS_SENTRY_DSN : Il s'agit du Nom de Source de Données (DSN) pour Sentry, qui est une plateforme de suivi des erreurs. Le DSN est un identifiant unique qui permet à Sentry d'identifier vers quel projet les événements doivent être envoyés.

    OC_LETTINGS_SENTRY_ENV : Cette variable spécifie l'environnement dans lequel les événements Sentry se produisent. Elle est utilisée pour différencier entre différents environnements (comme le développement, la mise en scène et la production) dans l'interface de Sentry.

    OC_LETTINGS_CSRF_TRUSTED_ORIGINS : Cette variable spécifie une liste d'origines de confiance pour la protection contre les attaques par falsification de requête intersite (CSRF) dans Django. Elle aide à prévenir les attaques CSRF en spécifiant quelles origines sont autorisées à effectuer des requêtes vers l'application Django. Chaque origine doit être ajoutée à cette liste.

.. code-block:: shell

   OC_LETTINGS_DEBUG = "Value_A"
   OC_LETTINGS_DJANGO_SECRET_KEY = "Value_B"
   OC_LETTINGS_ALLOWED_HOSTS = "Value_C,Value_D"
   OC_LETTINGS_SENTRY_DSN = "Value_E"
   OC_LETTINGS_SENTRY_ENV = "Value_F"
   OC_LETTINGS_CSRF_TRUSTED_ORIGINS = "Value_G,Value_H"

Faire le linting (Vérification de la syntaxe)
---------------------------------------------

Vérifiez que le code respecte les conventions de style et de syntaxe :

.. code-block:: shell

   flake8

Exécuter les tests
------------------

Exécutez les tests unitaires pour vous assurer que toutes les fonctionnalités fonctionnent correctement :

.. code-block:: shell

   python manage.py test

Vérifier la couverture des tests
--------------------------------

Évaluez la qualité des tests en vérifiant la couverture du code :

.. code-block:: shell

   python manage.py test coverage

Démarrer le serveur Django
--------------------------

Démarrez le serveur Django pour accéder au site web local :

.. code-block:: shell

   python manage.py runserver

Accéder au site
---------------

Dans la barre d'adresse du navigateur web, saisissez l'URL suivante pour accéder au site Orange County Lettings : http://localhost:8000.

-------------------------------------
