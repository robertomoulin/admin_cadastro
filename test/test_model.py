# -*- coding: utf-8 -*-
import unittest

from mysite.cadastro_rh.models import Cadastro


class CadastroTestCase(unittest.TestCase):

    def test_produto_deve_estar_registrado(self):
        import ipdb; ipdb.set_trace()
        self.nome = Cadastro.objects.create(nome="hansolo")
        self.assertEqual(self.nome, "hansolo")