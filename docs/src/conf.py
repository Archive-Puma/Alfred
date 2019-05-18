# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Autodoc -----------------------------------------------------------------

import os.path as ospath
from sys import path as pypath
currentdir = ospath.dirname(ospath.abspath(__file__))
pypath.insert(0, ospath.join(currentdir,'..','..','src'))
pypath.insert(1, ospath.join(currentdir,'..','..','lib'))

# -- Project information -----------------------------------------------------

project = 'Alfred'
copyright = '2019, Kike Fontán (@CosasDePuma)'
author = 'Kike Fontán (@CosasDePuma)'

with open(ospath.join(currentdir,'..','..','VERSION'),'r') as v:
    release = v.readline().strip()

master_doc="index"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = []

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'es'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
