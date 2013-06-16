# -*- coding: utf-8 -*-
from mysite.cadastro_rh.models import Cadastro

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import admin
# from django.http import HttpResponseRedirect
# from django.core.mail import send_mail


def enviar_email(modeladmin, request, queryset):
    enviar_email.short_description = "Enviar email"

    mail_string = ""
    for item in queryset:

        mail_string = mail_string + ">>" + str(item.email)


    # send_mail('titulo', email_list, 'roberto.rmoulin@gmail.com', email_list)
    # return HttpResponseRedirect("/login/enviar/")
    return render_to_response('contato.html', {'mail_string': mail_string}, context_instance=RequestContext(request, {}))


class ContatoAdmin(admin.ModelAdmin):
    list_display = ['_id', 'nome', 'email', 'departamento', 'cargo', 'status']
    list_filter = ['nome', 'cargo', 'datacadastro']
    search_fields = ['nome']
    actions = [enviar_email]
    save_on_top = True

admin.site.register(Cadastro, ContatoAdmin)



