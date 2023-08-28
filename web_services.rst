Web services
============

Most data in PGx is available programmatically via a REST API.

API reference
-------------

Each endpoint is described in the `API reference`_.

.. _API reference: https://gpcrdb.org/services/reference/

Examples
--------

Python 3 with requests
^^^^^^^^^^^^^^^^^^^^^^

This is the recommended approach. Requires installation of the `requests library`_.

.. _requests library: https://requests.readthedocs.io

::

    import requests

    # fetch a protein
    # coming soon

Python 3 with urllib
^^^^^^^^^^^^^^^^^^^^

::

    from urllib.request import urlopen
    import json

    # fetch a protein
    # coming soon

