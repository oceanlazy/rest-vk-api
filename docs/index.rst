.. REST VK API documentation master file, created by
   sphinx-quickstart on Wed May  2 04:00:45 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to REST VK API's documentation!
=======================================

Rest API for `VVK API
wrapper <https://github.com/vadimk2016/v-vk-api>`__.

Description
-----------

This is a simple REST API for VK API using the `VVK API
wrapper <https://github.com/vadimk2016/v-vk-api>`__, supported methods:
``users.get``, ``status.set``.

|Python3| |Release| |Documentation Status| |Build Status| |Coverage
Status| ### Install

::

    $ git clone https://github.com/vadimk2016/rest-vk-api.git
    $ pip install -r requirements.txt

Usage
-----

Create VK APP
^^^^^^^^^^^^^

To interact with the API, you need to
`create <https://vk.com/editapp?act=create>`__ an Standalone application
and save the following app data for later use: app id, service token,
login and password.

::

    python manage.py runserver

Access to API using httpie
^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    http --json GET http://127.0.0.1:8000/users/1?service_token=token_here
     {
      "response": [
        {
        "first_name": "Pavel",
        "id": 1,
        "last_name": "Durov"
        }
      ]
    }

    echo 'test status' | http --json POST "http://127.0.0.1:8000/status?app_id=123&login=123&password=pass
    {
        "response": 1
    }

    http --json DELETE "http://127.0.0.1:8000/status?app_id=123&login=123&password=pass
    {
        "response": 1
    }

Tests
-----

Tests will request methods and check JSON response from API, also to run
tests you need to provide ``config_test.json``. Then to run tests
execute: \`\`\` $ python manage.py test main.tests rest\_vk\_api

.. |Python3| image:: https://img.shields.io/badge/Python-3-brightgreen.svg
.. |Release| image:: https://img.shields.io/github/release/vadimk2016/rest-vk-api.svg
   :target: https://github.com/vadimk2016/rest-vk-api/releases
.. |Documentation Status| image:: https://readthedocs.org/projects/rest-vk-api/badge/?version=latest
   :target: http://rest-vk-api.readthedocs.io/en/latest/?badge=latest
.. |Build Status| image:: https://travis-ci.org/vadimk2016/rest-vk-api.svg?branch=master
   :target: https://travis-ci.org/vadimk2016/rest-vk-api
.. |Coverage Status| image:: https://coveralls.io/repos/github/vadimk2016/rest-vk-api/badge.svg
   :target: https://coveralls.io/github/vadimk2016/rest-vk-api