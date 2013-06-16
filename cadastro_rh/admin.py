# -*- coding: utf-8 -*-
from mysite.cadastro_rh.models import Cadastro

from django.contrib import admin
from django.http import HttpResponseRedirect
# from django.core.mail import send_mail


def enviar_email(modeladmin, request, queryset):
    enviar_email.short_description = "Enviar email"
    email_list = []
    for item in queryset:
        email = str(item.email)
        email_list.append(email)

    # send_mail('titulo', email_list, 'roberto.rmoulin@gmail.com', email_list)
    return HttpResponseRedirect("/login/enviar/%s/")


class ContatoAdmin(admin.ModelAdmin):
    list_display = ['_id', 'nome', 'email', 'departamento', 'cargo', 'status']
    list_filter = ['nome', 'cargo', 'datacadastro']
    search_fields = ['nome']
    actions = [enviar_email]
    save_on_top = True

admin.site.register(Cadastro, ContatoAdmin)



