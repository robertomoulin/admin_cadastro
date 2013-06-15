# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^login/enviar', 'mysite.cadastro_rh.views.enviar_email'),
    url(r'^login/', 'mysite.cadastro_rh.views.login'),
    url(r'^sair/', 'mysite.cadastro_rh.views.sair'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'.*\.js$', 'mysite.cadastro_rh.views.java_script'),
)
