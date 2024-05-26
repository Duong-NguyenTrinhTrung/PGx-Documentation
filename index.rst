.. PGx documentation master file, created by
   sphinx-quickstart on Fri Aug 25 09:53:56 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to PGxDB's documentation!
===================================

The PGxDB contains data, diagrams and web tools to facilitate pharmacogenomics research.

The `source code`_ and `source data`_ are freely available on `GitHub`_.

Below, a table overview of all the main pages and functionalities in PGxDB grouped by sections, along links to specific documentation pages, associated slides and video demonstrations.

.. _source code: https://github.com/Duong-NguyenTrinhTrung/pgx-db
.. _source data: https://github.com/Duong-NguyenTrinhTrung/PharmacogenomicsData
.. _GitHub: https://github.com


.. |Drug Video| image:: https://github.com/Duong-NguyenTrinhTrung/pgx-db/blob/main/static/home/logo/drug/drug2.png
                              :target: 

.. _Graphical overview: https://pgx-documentation.readthedocs.io/en/latest/graphical_overview.html
.. _ATC code browser: https://pgx-documentation.readthedocs.io/en/latest/atc_code.html
.. _Drug search: https://pgx-documentation.readthedocs.io/en/latest/drugs.html
.. _Disease search: https://pgx-documentation.readthedocs.io/en/latest/diseases.html
.. _Target search: https://pgx-documentation.readthedocs.io/en/latest/targets.html
.. _Variant search: https://pgx-documentation.readthedocs.io/en/latest/variants.html
.. _APIs: https://pgx-documentation.readthedocs.io/en/latest/web_services.html

.. |br| raw:: html

   <br>

.. csv-table:: **PAGES**
   :header:  "Page name", "Short description"
   :widths: 45 25 

   "`ATC code browser`_",  "The page allows browsing through the ATC code system, seeing drug profiles |br| as well as information indexed at an ATC code in 5 
   sections: |br| ** A tripartite network visualization for drugs, targets and disease as long as their interactions and associations |br| ** Statistics of drugs, targets, disease within the network |br| ** ATC-level network comparison |br| ** Pharmacogenomics information |br| ** Adverse drug reaction"
   "`Drug search`_", "The page provides search tool and displays basic information about a single or set |br| of drugs with links to the network visualization and drug statistics information"
   "`Disease search`_", "This page offers a search tool and presents essential details about diseases, |br| connections to drug-disease association networks, and 
   statistical data related to diseases."
   "`Target search`_",  "This page provides access to a search feature, view key details on |br| diseases, explore networks that map drug-disease associations, and 
   examine statistics concerning diseases"
   "`Variant search`_", "Section showing the variants, along with their effect prediction, burden |br| association statistics"
   "`APIs`_", "Section showing the API endpoints, along with sample Python |br| scripts, to help users download PGx data efficiently"



.. _user-docs:

.. toctree::
    :maxdepth: 2
    :caption: User documentation

    graphical_overview
    atc_code
    drugs
    diseases
    targets
    variants
    
    

.. _dev-docs:

.. toctree::
    :maxdepth: 2
    :caption: APIs

    web_services

.. _faqs-docs:

.. toctree::
    :maxdepth: 2
    :caption: FAQs

    faqs
    
    
.. _about-docs:

.. toctree::
    :maxdepth: 2
    :caption: About PGxDB

    about
    legal_notice
    contact
    
