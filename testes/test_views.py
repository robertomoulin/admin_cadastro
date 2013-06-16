import unittest
import requests
from mysite.settings import URL_SERVICE
import os


class TestViews(unittest.TestCase):

    def test_route_should_return_200(self):
        response = requests.get(os.path.join(URL_SERVICE, 'login/enviar'))
        status = response.status_code
        self.assertEqual(200, status)