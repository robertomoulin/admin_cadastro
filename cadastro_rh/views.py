# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponse


def index(request):
    return render_to_response('index.html')


def java_script(request):
    filename = request.path.strip("/")
    data = open(filename, "rb").read()
    return HttpResponse(data, mimetype="application/x-javascript")