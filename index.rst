.. PGx documentation master file, created by
   sphinx-quickstart on Fri Aug 25 09:53:56 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to PGx's documentation!
===================================

The GPCRdb contains data, diagrams and web tools for G protein-coupled receptors (GPCRs).
Users can browse all GPCR crystal structures and the largest collection of receptor mutants.
Diagrams can be produced and downloaded to illustrate receptor residues (snake-plot and helix box diagrams) and
relationships (phylogenetic trees). Reference (crystal) structure-based sequence alignments take into account helix
bulges and constrictions, display statistics of amino acid conservation and have been assigned generic
residue numbering for equivalent residues in different receptors.

The `source code`_ and `source data`_ are freely available on `GitHub`_.

Below, a table overview of all the different pages and functionalities in GPCRdb grouped by sections, along links to specific documentation pages, associated slides and video demonstrations.

.. _source code: https://github.com/protwis/protwis
.. _source data: https://github.com/protwis/gpcrdb_data
.. _GitHub: https://github.com
.. _Isberg et al. NAR 2014: https://doi.org/10.1093/nar/gkt1255
.. _Isberg et al. NAR 2016: https://doi.org/10.1093/nar/gkv1178


.. |Mutations Video| image:: https://justbewell.info/wp-content/uploads/2020/02/yt.png
                     :target: https://www.youtube.com/watch?v=XU9CnFuKDqk
.. |Receptor page Video| image:: https://justbewell.info/wp-content/uploads/2020/02/yt.png
                         :target: https://www.youtube.com/watch?v=LGq73spAZhc
.. |Receptor similarity Video| image:: https://justbewell.info/wp-content/uploads/2020/02/yt.png
                               :target: https://www.youtube.com/watch?v=_JYqES3B0yU
.. |Sequence alignment Video| image:: https://justbewell.info/wp-content/uploads/2020/02/yt.png
                              :target: https://www.youtube.com/watch?v=jxdrCKsXA4M


.. _Sequence alignments: https://docs.gpcrdb.org/sequences.html#structure-based-alignments
.. _Generic residue number tables: https://docs.gpcrdb.org/generic_numbering.html#generic-residue-numbering
.. _Genetic variants: https://docs.gpcrdb.org/variants.html#genetic-variants
.. _Receptor similarity: https://docs.gpcrdb.org/sequences.html#similarity-search-gpcrdb
.. _Structure coverage: https://docs.gpcrdb.org/structures.html#structures
.. _Structures: https://docs.gpcrdb.org/structures.html#structure-browser
.. _Structure models: https://docs.gpcrdb.org/structures.html#structure-models

.. |br| raw:: html

     <br>

.. csv-table:: **SEQUENCES**
   :header:  "Page name", "Video", "Slides", "Demo", "Reference", "Short description"
   :widths: 25 25 25 25 25 25

   "`Sequence alignments`_", "-", "-", "|Sequence alignment Video|", "`Isberg et al. NAR 2016`_ |br| `Kooistra et al. NAR 2021`_", "Provides sequence alignment analyses of receptors."
   "`Generic residue number tables`_", "-", "-", "-", "`Isberg et al. TiPS 2015`_", "Displays the generic residue number tables |br| for the single or set of receptors selected."
   "`Genetic variants`_", "-", "-", "-", "`Hauser et al. Cell 2018`_", "Section showing the variation coverage, |br| single receptor variants and the estimated |br| economic burden for drugs targeting GPCRs."
   "Isoforms", "-", "-", "-", "`Marti-Solano et al. Nature 2020`_", "Info page highlighting the number |br| of unique isoforms detected for |br| each receptor gene."


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