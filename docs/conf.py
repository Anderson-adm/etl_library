# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
sys.path.insert(0, os.path.abspath("../etl_library"))  # Aponta para a lib

project = 'etl_library'
copyright = '2025, Anderson'
author = 'Anderson'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",    # Gera doc automática a partir das docstrings
    "sphinx.ext.napoleon",   # Suporte a docstrings estilo Google/Numpy
    "sphinx.ext.viewcode",   # Links para o código-fonte
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'pt_BR'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"  # Tema do Read the Docs
html_static_path = ['_static']
