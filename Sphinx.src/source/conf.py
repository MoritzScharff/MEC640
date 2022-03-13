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
import os
import sys
sys.path.insert(0, os.path.abspath('.'))
#sys.path.insert(0, os.path.abspath('C:/Users/morit/Nextcloud/Documents/PostDoc/03_Training/Trainer/2021_Soft Robotics/Documents/Simulation/00_Introduction'))
#sys.path.append('C:/Users/morit/Nextcloud/Documents/PostDoc/03_Training/Trainer/2021_Soft Robotics/Documents/Simulation/01_Biomimetic')
#sys.path.append('C:/Users/morit/Nextcloud/Documents/PostDoc/03_Training/Trainer/2021_Soft Robotics/Documents/Simulation/02_Tensegrity')
#sys.path.append('C:/Users/morit/Nextcloud/Documents/PostDoc/03_Training/Trainer/2021_Soft Robotics/Documents/Simulation/03_Smart_materials_I')
#sys.path.append('C:/Users/morit/Nextcloud/Documents/PostDoc/03_Training/Trainer/2021_Soft Robotics/Documents/Simulation/04_Soft_gripping_I')
#sys.path.append('C:/Users/morit/Nextcloud/Documents/PostDoc/03_Training/Trainer/2021_Soft Robotics/Documents/Simulation/05_Soft_gripping_II')
#sys.path.append('C:/Users/morit/Nextcloud/Documents/PostDoc/03_Training/Trainer/2021_Soft Robotics/Documents/Simulation/06_Smart_materials_II')
#sys.path.append('C:/Users/morit/Nextcloud/Documents/PostDoc/03_Training/Trainer/2021_Soft Robotics/Documents/Simulation/07_Control_strategies_I')
#sys.path.append('C:/Users/morit/Nextcloud/Documents/PostDoc/03_Training/Trainer/2021_Soft Robotics/Documents/Simulation/08_Control_strategies_II')

# -- Project information -----------------------------------------------------

project = 'MEC 640'
copyright = '2022, Moritz Scharff'
author = 'Moritz Scharff'

# The full version, including alpha/beta/rc tags
release = '0.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon', 'sphinx.ext.viewcode'
              ]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

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
