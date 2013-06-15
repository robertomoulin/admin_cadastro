# -*- coding: utf-8 -*-
from mysite.cadastro_rh.models import Cadastro
from django.contrib import admin

def enviar_email(modeladmin, request, queryset):
    enviar_email.short_description = "Enviar email para os contatos selecionados"

class ContatoAdmin(admin.ModelAdmin):

    list_display = ['_id','nome','email','departamento','cargo','status']
    list_filter = ['nome','cargo', 'datacadastro']
    search_fields = ['nome']
    actions = [enviar_email]
    save_on_top = True

admin.site.register(Cadastro, ContatoAdmin)