Guide d'utilisation
====================

L'application oc_lettings_site propose une expérience de navigation conviviale pour ses utilisateurs, leur offrant un accès simple aux principales fonctionnalités. Voici un aperçu de la navigation sur le site :

Page d'Accueil
--------------

La page d'accueil constitue le premier point de contact des utilisateurs avec le site. Elle offre un aperçu global des fonctionnalités disponibles et propose des liens directs vers les sections principales telles que la liste des profils et la liste des locations.

+-------------------+------------------------------------------------+
| **URL et Params** | /                                              |
+-------------------+------------------------------------------------+
| **Méthode HTTP**  | GET                                            |
+-------------------+------------------------------------------------+
| **Description**   | Page HTML de l'accueil                         |
+-------------------+------------------------------------------------+

.. image:: _static/oc_lettings/home_page.png
    :align: center

Liste des Profils
-----------------

La liste des profils affiche tous les profils d'utilisateurs disponibles.

+------------------+-----------------------------------------------+
|   URL et Méth.   | URL : /profiles/                              |
|   HTTP**         | Méthode : GET                                 |
+------------------+-----------------------------------------------+
|   Réponse Att.   | La réponse est une page HTML (profiles/index  |
|                  | .html) affichant la liste des profils. Chaque |
|                  | profil est obtenu à partir du modèle Profile  |
|                  | qui est lié au modèle utilisateur standard de |
|                  | Django.                                       |
+------------------+-----------------------------------------------+

.. image:: _static/oc_lettings/profiles_page.png
    :align: center

Détails d'un Profil
--------------------

Cette interface affiche les détails d'un profil utilisateur spécifique. Le username est passé en tant que paramètre dans l'URL.

+------------------+---------------------------------------------+
|   URL et Méth    | URL : /profiles/<username>/                 |
|   HTTP           | Méthode : GET                               |
+------------------+---------------------------------------------+
|   Réponse Att.   | La réponse est une page HTML (profiles/     |
|                  | profile.html) affichant les détails du      |
|                  | profil spécifié. Les détails incluent le    |
|                  | nom d'utilisateur et la ville favorite.     |
+------------------+---------------------------------------------+

.. image:: _static/oc_lettings/profile_page.png
    :align: center

Liste des Locations
--------------------

La liste des locations affiche toutes les locations disponibles.

+-------------------+-----------------------------------------------+
|   Description     | Cette vue affiche une liste de toutes les     |
|                   | locations disponibles. Elle récupère toutes   |
|                   | les instances de Letting et les transmet au   |
|                   | template pour affichage.                      |
+-------------------+-----------------------------------------------+

.. image:: _static/oc_lettings/lettings_page.png
    :align: center

Détails d'une Location
-----------------------

Cette vue affiche les détails d'une location spécifique. Elle récupère une instance de Letting basée sur l'id fourni et transmet les détails au template.

+-------------------+----------------------------------------------------+
|   Description     | Cette vue affiche les détails d'une location       |
|                   | spécifique. Elle récupère une instance de Letting  |
|                   | basée sur l'id fourni et transmet les détails au   |
|                   | template.                                          |
+-------------------+----------------------------------------------------+

.. image:: _static/oc_lettings/letting_page.png
    :align: center

Accès Administrateur
---------------------

En tant qu'administrateur, vous bénéficiez d'un accès privilégié à certaines fonctionnalités de l'application via l'interface d'administration Django.

+--------------------+------------------------------------------------+
| **URL**            | /admin/                                        |
+--------------------+------------------------------------------------+
| **Méthode**        | GET pour l'accès, POST pour les interactions   |
|                    | (ajout, modification, suppression des données).|
+--------------------+------------------------------------------------+

.. image:: _static/oc_lettings/admin_page.png
    :align: center

Gestion des Données
--------------------

Les administrateurs peuvent effectuer les actions suivantes dans l'interface d'administration :

- Ajouter de nouvelles instances pour les modèles Letting et Profile.
- Modifier les données existantes des instances de ces modèles.
- Supprimer des instances si nécessaire.

Sécurité et Accès
--------------------

L'accès à l'interface d'administration est restreint aux utilisateurs ayant des droits d'administrateur. Il est recommandé de gérer attentivement les comptes administrateurs pour maintenir la sécurité.
