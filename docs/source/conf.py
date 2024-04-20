# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Orange County Lettings'
copyright = '2024, Mohand Arezki Lahlou'
author = 'Mohand Arezki Lahlou'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'fr'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ['_static']
html_theme = "sphinx_rtd_theme"

# Personnalisation du thème
html_theme_options = {
    "logo_only": True,  # Afficher uniquement le logo dans la barre de navigation
    "display_version": True,  # Afficher la version de la documentation
    "prev_next_buttons_location": "bottom",  # Déplacez les boutons de navigation en bas de page
    "style_external_links": True,  # Appliquez le style aux liens externes
    "style_nav_header_background": "#2980B9",  # Couleur de fond de l'en-tête de navigation
    "navigation_depth": 2,  # Profondeur de navigation dans la table des matières
}

# Définissez le logo du projet (remplacez "logo.png" par le chemin de votre logo)
# html_logo = "_static/oc_logo.png"

# Personnalisez le pied de page (facultatif)
html_footer = """
<div class="footer">
    <p>&copy; {}</p>
</div>
""".format(
    author
)

html_css_files = [
    "css/custom.css",
]
