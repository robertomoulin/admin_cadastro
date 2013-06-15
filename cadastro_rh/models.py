# -*- coding: utf-8 -*-
from django.db import models


STATUS_LIST = (('A','Ativo'),('I','Inativo'),)


class Cadastro(models.Model):

        _id = models.AutoField(primary_key=True)
        nome = models.CharField(max_length=255)
        foto = models.ImageField(upload_to='cadastros/%Y',null=True,blank=True)
        email = models.EmailField(max_length=200)
        status = models.CharField(max_length=1,choices=STATUS_LIST)
        telefone = models.CharField(max_length=20)
        datanascimento = models.DateField(verbose_name='Data de Nascimento',null=True,blank=True)
        departamento = models.CharField(max_length=30)
        cargo = models.CharField(max_length=30)
        datacadastro = models.DateTimeField(auto_now_add=True)

        def __unicode__(self):
            return self.nome

        class Meta:
            db_table = u'contato'
            verbose_name = 'Contato'
            verbose_name_plural = 'Contatos'
            ordering = ['nome']
