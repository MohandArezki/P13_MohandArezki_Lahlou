Réorganiser l'architecture modulaire
====================================

- Création d'une nouvelle application "lettings", contenant les modèles "Address" et "Letting".
- Création d'une nouvelle application "profiles", contenant le modèle "Profile".
- Copie des données de la base vers les nouvelles tables.
- Suppression des anciennes tables de la base de données.
- Déplacement cohérent des templates dans les nouvelles applications.
- Déplacement des URL de "lettings", "profiles", "lettings_index" et "profiles_index" de "oc_lettings_site" vers les nouvelles applications.
- Création des espaces de nom pour les URL des deux nouvelles applications.
- Renommage de "lettings_index.html" en "index.html" et de la vue "lettings_index" en "index". Renommage de "profiles_index.html" en "index.html" et de la vue "profiles_index" en "index".
- Suppression des fichiers inutiles dans l’application "oc_lettings_site".

Ci-dessous la nouvelle structure du projet :

.. code-block:: bash

    .
    ├── Dockerfile
    ├── lettings
    │   ├── admin.py
    │   ├── apps.py
    │   ├── __init__.py
    │   ├── migrations
    │   │   ├── 0001_initial.py
    │   │   └── __init__.py
    │   ├── models.py
    │   ├── templates
    │   │   └── lettings
    │   │       ├── index.html
    │   │       └── letting.html
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── manage.py
    ├── oc_lettings_site
    │   ├── apps.py
    │   ├── asgi.py
    │   ├── __init__.py
    │   ├── migrations
    │   │   └── __init__.py
    │   ├── settings.py
    │   ├── tests.py
    │   ├── urls.py
    │   ├── views.py
    │   └── wsgi.py
    ├── oc-lettings-site.sqlite3
    ├── profiles
    │   ├── admin.py
    │   ├── apps.py
    │   ├── __init__.py
    │   ├── migrations
    │   │   ├── 0001_initial.py
    │   │   └── __init__.py
    │   ├── models.py
    │   ├── templates
    │   │   └── profiles
    │   │       ├── index.html
    │   │       └── profile.html
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── README.md
    ├── requirements.txt
    ├── setup.cfg
    ├── static
    │   ├── assets
    │   │   ├── fonts
    │   │   │   └── metropolis
    │   │   │       ├── Metropolis-BlackItalic.otf
    │   │   │       ├── Metropolis-Black.otf
    │   │   │       ├── Metropolis-BoldItalic.otf
    │   │   │       ├── Metropolis-Bold.otf
    │   │   │       ├── Metropolis-ExtraBoldItalic.otf
    │   │   │       ├── Metropolis-ExtraBold.otf
    │   │   │       ├── Metropolis-ExtraLightItalic.otf
    │   │   │       ├── Metropolis-ExtraLight.otf
    │   │   │       ├── Metropolis-LightItalic.otf
    │   │   │       ├── Metropolis-Light.otf
    │   │   │       ├── Metropolis-MediumItalic.otf
    │   │   │       ├── Metropolis-Medium.otf
    │   │   │       ├── Metropolis-RegularItalic.otf
    │   │   │       ├── Metropolis-Regular.otf
    │   │   │       ├── Metropolis-SemiBoldItalic.otf
    │   │   │       ├── Metropolis-SemiBold.otf
    │   │   │       ├── Metropolis-ThinItalic.otf
    │   │   │       ├── Metropolis-Thin.otf
    │   │   │       └── SIL Open Font License.txt
    │   │   └── img
    │   │       └── logo.png
    │   ├── css
    │   │   └── styles.css
    │   └── js
    │       └── scripts.js
    └── templates
        ├── 404.html
        ├── 500.html
        ├── base.html
        └── index.html

    18 directories, 63 files

