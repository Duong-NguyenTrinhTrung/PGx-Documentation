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


.. _ATC code browser:
.. _Drug browser: 
.. _Disease browser:
.. _Target browser: 
.. _Variant browser: https://docs.gpcrdb.org/variants.html#genetic-variants
.. _APIs: 

.. |br| raw:: html

     <br>

.. csv-table:: **PAGES**
   :header:  "Page name", "Demo video", "Short description"
   :widths: 45 25 25

   "`ATC code browser`_", "-", "The page allows browsing through the ATC code system, seeing drug profiles as well as a tripartite network visualization for drugs, 
   targets and disease nodes indexed at an ATC code "
   "`Drug browser`_", "|Drug Video|", "The page provides search tool and displays basic information about a single or set of drugs with links to the network visualization 
   and drug statistics information"
   "`Disease browser`_", "-", "This page offers a search tool and presents essential details about diseases, connections to drug-disease association networks, and 
   statistical data related to diseases."
   "`Target browser`_", "-", "This page provides access to a search feature, view key details on diseases, explore networks that map drug-disease associations, and examine 
   statistics concerning diseases"
   "`Variant browser`_", "-", "Section showing the variants, along with their effect prediction, burden association statistics"
   "`APIs`_", "-", "Section showing the API endpoints, along with sample Python scripts, to help users download PGx data efficiently"


The documentation is organised into four sections:

* :ref:`user-docs`
* :ref:`video-tut-docs`
* :ref:`dev-docs`
* :ref:`about-docs`

.. _user-docs:

.. toctree::
    :maxdepth: 2
    :caption: User documentation

    drugs
    targets
    variants
    
.. _video-tut-docs:

.. toctree::
    :maxdepth: 2
    :caption: Video tutorials

    browsing_drug_page
    browsing_target_page
    browsing_variant_page
    browsing_API_page
    

.. _dev-docs:

.. toctree::
    :maxdepth: 2
    :caption: Developer documentation

    web_services
    contributing
    
.. _about-docs:

.. toctree::
    :maxdepth: 2
    :caption: About PGx

    about
    contact
    citing_PGx
    external_PGx_sites
