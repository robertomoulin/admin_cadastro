import unittest
import requests
from mysite.settings import URL_SERVICE
import os


class TestRote(unittest.TestCase):

    def test_login_route_should_return_200(self):
        response = requests.get(os.path.join(URL_SERVICE, 'login/'))
        status = response.status_code
        self.assertEqual(200, status)

    def test_logout_route_should_return_200(self):
        response = requests.get(os.path.join(URL_SERVICE, 'sair/'))
        status = response.status_code
        self.assertEqual(200, status)

    def test_email_route_should_return_200(self):
        response = requests.get(os.path.join(URL_SERVICE, 'login/enviar'))
        status = response.status_code
        self.assertEqual(200, status)

    def test_admin_route_should_return_200(self):
        response = requests.get(os.path.join(URL_SERVICE, 'admin/'))
        status = response.status_code
        self.assertEqual(200, status)
