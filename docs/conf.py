# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
from unittest.mock import MagicMock

sys.path.insert(0, os.path.abspath("../repos/mlops-data-processor"))
sys.path.insert(0, os.path.abspath("../repos/mlops-pipeline-api"))
sys.path.insert(2, os.path.abspath("../repos/mlops-streamlit-ui"))

# Get all dependencies
autodoc_mock_imports = ["pandas", "seaborn", "matplotlib",
                        "utils", "celery", "sklearn", "joblib", "tasks",
                        "mlflow", "opentelemetry-distro",
                        "scikit-learn", "sqlalchemy", "psycop2-binary",
                        "fastparquet", "optuna", "boto3", "botocore",
                        "streamlit", "streamlit-authenticator", "loguru", "pydantic",
                        "requests", "opentelemetry-exporter-otlp"]

add_module_names = False
# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


# -- Project information -----------------------------------------------------

project = "FH-SWF MLOPS"
copyright = ""
author = ""

# The full version, including alpha/beta/rc tags
release = ""

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx_copybutton",
    "sphinx.ext.intersphinx",
    'sphinxcontrib.mermaid'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "analytics_anonymize_ip": False,
    "logo_only": False,
    "display_version": True,
    "prev_next_buttons_location": "bottom",
    "style_external_links": False,
    "vcs_pageview_mode": "",
    "style_nav_header_background": "black",
    # Toc options
    "collapse_navigation": True,
    "sticky_navigation": True,
    "navigation_depth": 4,
    "includehidden": True,
    "titles_only": False,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css". Test
html_static_path = ["_static"]
html_css_files = ['css/hacks.css']


def skip(app, what, name, obj, would_skip, options):
    if name == "__init__":
        return False
    return would_skip


def setup(app):
    app.connect("autodoc-skip-member", skip)
    app.add_css_file("css/my_theme.css")
