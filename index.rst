.. PGx documentation master file, created by
   sphinx-quickstart on Fri Aug 25 09:53:56 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to PGx's documentation!
===================================

The PGx contains data, diagrams and web tools to facilitate pharmacogenomics research.

The `source code`_ and `source data`_ are freely available on `GitHub`_.

Below, a table overview of all the different pages and functionalities in PGx grouped by sections, along links to specific documentation pages, associated slides and video demonstrations.

.. _source code: https://github.com/Duong-NguyenTrinhTrung/pgx-db
.. _source data: https://github.com/Duong-NguyenTrinhTrung/PharmacogenomicsData
.. _GitHub: https://github.com


.. |Drug Video| image:: https://github.com/Duong-NguyenTrinhTrung/pgx-db/blob/main/static/home/logo/drug/drug2.png
                              :target: 


.. _ATC code browser: https://pgx-documentation.readthedocs.io/en/latest/drugs.html
.. _Drug browser: https://pgx-documentation.readthedocs.io/en/latest/drugs.html
.. _Disease browser:
.. _Target browser: https://pgx-documentation.readthedocs.io/en/latest/targets.html
.. _Variant browser: https://pgx-documentation.readthedocs.io/en/latest/variants.html
.. _APIs: https://pgx-documentation.readthedocs.io/en/latest/web_services.html

.. |br| raw:: html

     <br>

.. csv-table:: **PAGES**
   :header:  "Page name", "Demo video", "Short description"
   :widths: 45 25 25

   "`ATC code browser`_", "-", "The page allows browsing through the ATC code system, seeing drug profiles |br| as well as information indexed at an ATC code in 4 
   sections: |br|   - a tripartite network visualization for drugs, targets and disease nodes; |br|   - statistics of drugs, targets, disease within the network; |br|   - ATC-level network comparison; |br|   - pharmacogenomics information"
   "`Drug browser`_", "|Drug Video|", "The page provides search tool and displays basic information about |br| a single or set of drugs with links to the network 
   visualization |br| and drug statistics information"
   "`Disease browser`_", "-", "This page offers a search tool and presents essential details about diseases, |br| connections to drug-disease association networks, and 
   statistical data related to diseases."
   "`Target browser`_", "-", "This page provides access to a search feature, view key details on diseases, |br| explore networks that map drug-disease associations, and 
   examine statistics concerning diseases"
   "`Variant browser`_", "-", "Section showing the variants, along with their effect prediction, burden |br| association statistics"
   "`APIs`_", "-", "Section showing the API endpoints, along with sample Python |br| scripts, to help users download PGx data efficiently"


The documentation is organised into four sections:

* :ref:`user-docs`
* :ref:`video-tut-docs`
* :ref:`dev-docs`
* :ref:`about-docs`

.. _user-docs:

.. toctree::
    :maxdepth: 2
    :caption: User documentation

    atc codes
    drugs
    diseases
    targets
    variants
    
.. _video-tut-docs:

.. toctree::
    :maxdepth: 2
    :caption: Video tutorials

    browsing_atc_code_page
    browsing_drug_page
    browsing_target_page
    browsing_variant_page
    
    

.. _dev-docs:

.. toctree::
    :maxdepth: 2
    :caption: API

    web_services
    
    
.. _about-docs:

.. toctree::
    :maxdepth: 2
    :caption: About PGx

    about
    contact
    citing_PGx
    external_PGx_sites
