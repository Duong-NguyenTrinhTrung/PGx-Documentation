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

    def download_gene_data(gene_ids):
    base_url = "X"  

    for gene_id in gene_ids:
        url = f"{base_url}/gene/variant/{gene_id}/"
        response = requests.get(url)

        if response.status_code == 200:
            # Assuming the response contains JSON data, you can use response.json() to access the data
            gene_data = response.json()
            
            # Process or save the gene_data as needed
            print(f"Downloaded data for gene ID {gene_id}: {gene_data}")
        else:
            print(f"Failed to download data for gene ID {gene_id}. Status code: {response.status_code}")

    # Example usage:
    gene_ids_to_download = ["gene_id1", "gene_id2", "gene_id3"]  # List of your gene_id here
    download_gene_data(gene_ids_to_download)

Python 3 with urllib
^^^^^^^^^^^^^^^^^^^^

::

    from urllib.request import urlopen
    import json

    # fetch a protein
    # coming soon

