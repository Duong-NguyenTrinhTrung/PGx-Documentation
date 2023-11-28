APIs
============

Most data in PGx is available programmatically via a REST API.

List of API endpoints
-------------

Each endpoint is described in the `API reference`_.

.. _API reference: http://localhost:8000/swagger/

API sample scripts
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

