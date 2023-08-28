.. PGx documentation master file, created by
   sphinx-quickstart on Fri Aug 25 09:53:56 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to PGx's documentation!
===================================

The PGx contains data, diagrams and web tools to facilitate pharmacogenomics research.

The `source code`_ and `source data`_ are freely available on `GitHub`_.

Below, a table overview of all the different pages and functionalities in PGx grouped by sections, along links to specific documentation pages, associated slides and video demonstrations.

.. _source code: https://github.com/protwis/protwis
.. _source data: https://github.com/protwis/gpcrdb_data
.. _GitHub: https://github.com
.. _Isberg et al. NAR 2014: https://doi.org/10.1093/nar/gkt1255
.. _Isberg et al. NAR 2016: https://doi.org/10.1093/nar/gkv1178


.. |Drug Video| image:: https://justbewell.info/wp-content/uploads/2020/02/yt.png
                              :target: https://www.youtube.com/watch?v=jxdrCKsXA4M


.. _Drugs: https://docs.gpcrdb.org/sequences.html#structure-based-alignments
.. _Targets: https://docs.gpcrdb.org/generic_numbering.html#generic-residue-numbering
.. _Genetic variants: https://docs.gpcrdb.org/variants.html#genetic-variants

.. |br| raw:: html

     <br>

.. csv-table:: **SEQUENCES**
   :header:  "Page name", "Video", "Slides", "Demo", "Reference", "Short description"
   :widths: 25 25 25 25 25 25

   "`Drugs`_", "-", "-", "|Drug Video|", "`Isberg et al. NAR 2016`_ |br| `Kooistra et al. NAR 2021`_", "Provides drug page for a single or set of drugs."
   "`Targets`_", "-", "-", "-", "`Isberg et al. TiPS 2015`_", "Displays the Targets |br| for the single or set of drugs selected."
   "`Genetic variants`_", "-", "-", "-", "`Hauser et al. Cell 2018`_", "Section showing the variants, |br| along with their effect prediction |br| and association statistics across almost 3000 phenotypes."


The documentation is organised into three sections:

* :ref:`user-docs`
* :ref:`val-docs`
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

.. _val-docs:

.. toctree::
    :maxdepth: 2
    :caption: Data collection and validation

    data_collection
    data_validation
    
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
    