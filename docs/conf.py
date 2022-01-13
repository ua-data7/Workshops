# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys

import contextlib
from distutils.version import LooseVersion
import os
from os.path import dirname, join
import sys

#import yaml

#import sphinx_material



# Uncommented next line
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('../'))



# -- Project information -----------------------------------------------------

project = 'UA DATA7 Workshops'
copyright = 'UA DATA7, The University of Arizona'
authors = 'C. Lizarraga'

# The full version, including alpha/beta/rc tags
release = '0.5'
author='Carlos Lizarraga'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosummary",
    "sphinx.ext.extlinks"
]

napoleon_google_docstring = False
napoleon_use_param = False
napoleon_use_ivor = True


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'

html_theme_options = {
#     "use_download_button": True,
#     "home_page_in_toc": True
 }

# Logo here
#html_static_path = ['_static']

#html_logo = "images/tribs_meshfig_med.jpg"
#html_theme_options = {
#    'logo_only': False,
#    'display_version': False,
#}


# Added this for tables appearance on small screens
def setup(app):
    app.add_css_file('theme_overrides.css')

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
