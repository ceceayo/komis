# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# Project information
project = "KomisPLUS"
copyright = "2024, Ceayo"
author = "Ceayo"
release = "0.0.0"

# General configuration
extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
]

# The suffix of source filenames.
source_suffix = [
    ".rst",
    ".md",
]
templates_path = [
    "_templates",
]
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
]

# Options for HTML output
html_theme = "furo"
html_static_path = ["_static"]
