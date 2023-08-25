# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import sphinx_rtd_theme


project = 'PGx'
copyright = '2023, Duong, Nguyen'
author = 'Duong, Nguyen'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx_rtd_theme', 'sphinx.ext.todo', 'sphinx.ext.viewcode', 'sphinx.ext.autodoc']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']


The documentation is organised into three sections:

* :ref:`user-docs`
* :ref:`dev-docs`
* :ref:`about-docs`

.. _user-docs:

.. toctree::
    :maxdepth: 2
    :caption: User documentation

    receptors
    ligands
    signalproteins
    sequences
    sequence_signature
    structures
    structure_comparison
    constructs
    mutations
    biasedsignaling
    sites
    generic_numbering
    drugs
    nhs
    variants

.. _dev-docs:

.. toctree::
    :maxdepth: 2
    :caption: Developer documentation

    web_services
    contributing
    local_installation
    coding_style
    git_workflow
    reload_database
    building_a_database

.. _about-docs:

.. toctree::
    :maxdepth: 2
    :caption: About GPCRdb

    about
    contact
    contributors
    citing
    acknowledgements
    legal_notice
    meetings
    linking
    external_sites
