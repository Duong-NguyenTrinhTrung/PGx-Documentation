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


.. _Drugs: 
.. _Targets: 
.. _Genetic variants: https://docs.gpcrdb.org/variants.html#genetic-variants

.. |br| raw:: html

     <br>

.. csv-table:: **PAGES**
   :header:  "Page name", "Video", "Demo", "Short description"
   :widths: 25 25 25 25

   "`Drugs`_", "-", "|Drug Video|", "Provides drug page for a single or set of drugs along with |br| the ATC code system"
   "`Targets`_", "-", "-", "Displays the Targets |br| for the single or set of drugs selected."
   "`Genetic variants`_", "-", "-", "Section showing the variants, |br| along with their effect prediction, |br| burden association statistics and drug response information"
   "`APIs`_", "-", "-", "Section showing the API endpoints, |br| along with sample Python scripts, |br| to help users download PGx data efficiently"


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
