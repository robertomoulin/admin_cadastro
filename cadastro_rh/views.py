# -*- coding:utf-8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout, login as authlogin
from django.template import RequestContext
from django import forms

from django.core.mail import send_mail

from cadastro_rh.models import Cadastro


def login(request):
    if request.user.id:
        return render_to_response('logado.html',{},context_instance=RequestContext(request, {}))

    if request.POST:
        emailUser = request.POST.get('email')
        senhaUser = request.POST.get('senha')

        auth = authenticate(username=emailUser, password=senhaUser)
        if auth is not None:
            if auth.is_active:
                authlogin(request,auth)
                lista_cadastro = Cadastro.objects.all().order_by('datacadastro')

                return render_to_response('logado.html', {'lista_cadastro': lista_cadastro, 'macaca': 'macaca'}, context_instance=RequestContext(request))

    return render_to_response('login.html',{},context_instance=RequestContext(request, {}))


def sair(request):
    logout(request)
    return render_to_response('login.html')



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


def enviar_email(request):
    if request.method == 'POST':
        checkbox_mail = request.POST.get('nome')

        form = FormContato(request.POST)
        if form.is_valid():
            form.enviar()
    else:
        form = FormContato()
    return render_to_response('contato.html',locals(),context_instance=RequestContext(request, {}))



def java_script(request):
    filename = request.path.strip("/")
    data = open(filename, "rb").read()
    return HttpResponse(data, mimetype="application/x-javascript")


def tela_cadastro(request):
    return render_to_response('tela_cadastro.html', mimetype="text/html")
