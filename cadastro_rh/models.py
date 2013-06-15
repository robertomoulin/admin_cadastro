# -*- coding: utf-8 -*-
from django import forms
from django.db import models
from django.core.mail import send_mail


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


class FormContato(forms.Form):
    mensagem = forms.Field(widget=forms.Textarea)
    email = forms.EmailField(required=False)

    def enviar(self):
        titulo = 'Mensagem enviada pelo site'
        destino = 'roberto.rmoulin@gmail.com'
        texto = "aiefiufhaeuuhaefhuafhu"

        send_mail(  subject=titulo,
                    message=texto,
                    from_email=destino,
                    recipient_list=[destino],
        )