# -*- conding: utf-8 -*-
import unittest

from mysite.cadastro_rh.models import Cadastro, FormContato


class CadastroTestCase(unittest.TestCase):

    def setUp(self):
        self.cadastro = Cadastro.objects.create(nome="hansolo",
                                                email="hansolo@gmail.com",
                                                departamento="RH",
                                                cargo="atirador",
                                                status='Ativo')

    def test_should_return_expected_name(self):
        expected = "hansolo"
        self.assertEqual(expected, self.cadastro.nome)

    def test_should_return_expected_email(self):
        expected = "hansolo@gmail.com"
        self.assertEqual(expected, self.cadastro.email)

    def test_should_return_expected_cargo(self):
        expected = "atirador"
        self.assertEqual(expected, self.cadastro.cargo)

    def test_should_return_expected_departamento(self):
        expected = "RH"
        self.assertEqual(expected, self.cadastro.departamento)

    def test_should_return_expected_status(self):
        expected = "Ativo"
        self.assertEqual(expected, self.cadastro.status)

    def tearDown(self):
        self.cadastro.delete()


class FormContatoTestCase(unittest.TestCase):

    def test_should_send_email(self):
        self.form = FormContato()
        email_list = "rh.chewbacca@gmail.com"
        texto = "Ola colaboradores"
        status = self.form.enviar(email_list, texto)
        self.assertTrue(status)
