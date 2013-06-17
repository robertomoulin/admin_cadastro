# -*- coding:utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
# from django.contrib.auth import authenticate, logout, login as authlogin

from mysite.cadastro_rh.models import FormContato
# from cadastro_rh.models import Cadastro


"""
Estava fazendo o login do admin tbm pelo front no html da aplicacao.
Demoraram a responder minha dúvida, fiquei com medo de perder tempo
implementando de forma errada, aí eu comecei a implementar os 2 modos,
pelo admin e pelo html da aplicacao.
(Agora que vi o email de vcs, to fazendo só o admin.)

Não cheguei a terminar por completo a versao pelo html da aplicacao,
mas vou deixar o código que fiz aqui comentado .
"""


def login(request):
    # if request.user.id:
    #     return render_to_response('logado.html', {}, context_instance=RequestContext(request, {}))

    # if request.POST:
    #     emailUser = request.POST.get('email')
    #     senhaUser = request.POST.get('senha')

    #     auth = authenticate(username=emailUser, password=senhaUser)
    #     if auth is not None:
    #         if auth.is_active:
    #             authlogin(request, auth)
    #             lista_cadastro = Cadastro.objects.all().order_by('datacadastro')

    #             return render_to_response('logado.html', {'lista_cadastro': lista_cadastro, 'macaca': 'macaca'}, context_instance=RequestContext(request))

    return render_to_response('login.html', {}, context_instance=RequestContext(request, {}))


def sair(request):
    # logout(request)
    return render_to_response('login.html')


def enviar_email(request):
    if request.method == 'POST':
        form = FormContato(request.POST)
        email_list = request.POST.get('email')
        texto = request.POST.get('texto')
        form.enviar(email_list, texto)
        return render_to_response('sucesso.html', locals(), context_instance=RequestContext(request, {}))
    else:
        form = FormContato()
        return render_to_response('contato.html', locals(), context_instance=RequestContext(request, {}))


def java_script(request):
    filename = request.path.strip("/")
    data = open(filename, "rb").read()
    return HttpResponse(data, mimetype="application/x-javascript")
