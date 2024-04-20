===============================
Structure de la base de données
===============================

Base de données et structure des modèles
-----------------------------------------

**Type de base de données**: SQLite3

SQLite est une bibliothèque C fournissant une base de données légère basée sur le disque, sans nécessiter un processus de serveur séparé. L'accès se fait via une variante non standard de SQL. C'est une base de données autonome, native à Python et utilisée par Django par défaut lors de la création de nouveaux projets.

Contenu de la base de données
------------------------------

1. **Profils des utilisateurs/clients**: Chaque profil contient un identifiant (non affiché), une ville favorite et une référence à un utilisateur (non affichée). Les informations utilisateur telles que le prénom, le nom, l'e-mail et la ville préférée sont stockées dans la table "auth_user".

2. **Letting**: Liste de propriétés avec un titre correspondant. Chaque letting possède un identifiant (non affiché) et un titre, et est lié à une adresse (non affichée).

3. **Adresse**: Détails des adresses des biens. Chaque adresse possède un identifiant (non affiché), un numéro, une rue, une ville, un état, un code postal et un code ISO de pays.

Instructions pour l'accès à la base de données
-----------------------------------------------

#. Assurez-vous d'être dans le répertoire du projet :

.. code-block:: shell

   cd [Nom_du_répertoire_du_projet]

#. Ouvrez une session Shell pour SQLite :

.. code-block:: shell

   sqlite3

#. Connectez-vous à la base de données :

.. code-block:: shell

   .open oc-lettings-site.sqlite3

#. Affichez les tables dans la base de données :

.. code-block:: shell

   .tables

#. Affichez les colonnes dans le tableau des profils :

.. code-block:: shell

   PRAGMA table_info("profiles_profile");

#. Lancez une requête sur la table des profils pour filtrer uniquement les enregistrements où la valeur de la colonne favorite_city commence par la lettre 'B' :

.. code-block:: shell

   select user_id, favorite_city from profiles_profile where favorite_city like 'B%';
   