import os
import json
from urllib.parse import urlencode

from django.test import TestCase
from rest_framework.response import Response


def get_credentials():
    cfg_path = os.path.join(os.path.dirname(__file__), 'config_test.json')
    if os.path.isfile(cfg_path):
        with open(cfg_path) as f:
            return json.load(f)
    return {}


class TestViews(TestCase):
    credentials = get_credentials()

    def test_get_user(self):
        url_params = {'service_token': self.credentials.get('service_token')}
        url = '/users/1?{}'.format(urlencode(url_params))
        response = self.client.get(url)
        self.assertIsInstance(response, Response)
        self.assertIsInstance(response.data, dict)
        self.assertIn('response', response.data)
        self.assertIn('Durov', response.data['response'][0]['last_name'])

    def test_set_status(self):
        url_params = {'app_id': self.credentials.get('app_id'),
                      'login': self.credentials.get('login'),
                      'password': self.credentials.get('password')}
        url = '/status?{}'.format(urlencode(url_params))
        response = self.client.post(url, {'test status': None})
        self.assertIsInstance(response, Response)
        self.assertIsInstance(response.data, dict)
        self.assertIn('response', response.data)
        self.assertEqual({'response': 1}, response.data)

    def test_clear_status(self):
        url_params = {'app_id': self.credentials.get('app_id'),
                      'login': self.credentials.get('login'),
                      'password': self.credentials.get('password')}
        url = '/status?{}'.format(urlencode(url_params))
        response = self.client.delete(url)
        self.assertIsInstance(response, Response)
        self.assertIsInstance(response.data, dict)
        self.assertIn('response', response.data)
        self.assertEqual({'response': 1}, response.data)
