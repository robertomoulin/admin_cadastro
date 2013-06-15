# -*- coding: utf-8 -*-
from mysite.cadastro_rh.models import Cadastro

from django.shortcuts import render_to_response
from django.contrib import admin
from django.core.mail import send_mail
from django.template import RequestContext
from django import forms


def enviar_email(modeladmin, request, queryset):
    enviar_email.short_description = "Enviar email"
    email_list = []
    for item in queryset:
        email = item.email
        email_list.append(email)

    send_mail('titulo', email_list, 'contato_rh@gmail.com', email_list)



# class FormContato(forms.Form):
#     mensagem = forms.Field(widget=forms.Textarea)

#     def enviar(self, email_list):
#         titulo = 'Mensagem do RH'
#         texto = """ Nome: %(nome)s E-mail: %(email)s Mensagem:%(mensagem)s""" % self.cleaned_data

#         send_mail(titulo, texto, 'contato_rh@gmail.com', email_list)



class ContatoAdmin(admin.ModelAdmin):
    list_display = ['_id','nome','email','departamento','cargo','status']
    list_filter = ['nome','cargo', 'datacadastro']
    search_fields = ['nome']
    actions = [enviar_email]
    save_on_top = True

admin.site.register(Cadastro, ContatoAdmin)