# -*- coding:utf-8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout, login as authlogin
from django.template import RequestContext


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

                    return render_to_response('logado.html',{},context_instance=RequestContext(request, {}))

        return render_to_response('login.html',{},context_instance=RequestContext(request, {}))


def sair(request):
        logout(request)
        return render_to_response('login.html',{},context_instance=RequestContext(request, {}))



def java_script(request):
    filename = request.path.strip("/")
    data = open(filename, "rb").read()
    return HttpResponse(data, mimetype="application/x-javascript")


def tela_cadastro(request):
    return render_to_response('tela_cadastro.html', mimetype="text/html")
