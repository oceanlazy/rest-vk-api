# REST VK API

Rest API for [VVK API wrapper](https://github.com/vadimk2016/v-vk-api).

## Description

This is a simple REST API for VK API using the [VVK API wrapper](https://github.com/vadimk2016/v-vk-api), supported methods: `users.get`, `status.set`.

![Python3](https://img.shields.io/badge/Python-3-brightgreen.svg)
[![Release](https://img.shields.io/github/release/vadimk2016/rest-vk-api.svg)](https://github.com/vadimk2016/rest-vk-api/releases)
[![Build Status](https://travis-ci.org/vadimk2016/rest-vk-api.svg?branch=master)](https://travis-ci.org/vadimk2016/rest-vk-api)
[![Coverage Status](https://coveralls.io/repos/github/vadimk2016/rest-vk-api/badge.svg)](https://coveralls.io/github/vadimk2016/rest-vk-api)
### Install

```
$ git clone https://github.com/vadimk2016/rest-vk-api.git
$ pip install -r requirements.txt
```

## Usage

#### Create VK APP
    
To interact with the API, you need to [create](https://vk.com/editapp?act=create) an Standalone application and save the following app data for later use: app id, service token, login and password.


    python manage.py runserver
    
#### Access to API using httpie

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
## Tests

Tests will request methods and check JSON response from API, also to run tests you need to provide `config_test.json`. Then to run tests execute:
```
$ python manage.py test main.tests rest_vk_api