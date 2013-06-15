# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^login/enviar', 'mysite.cadastro_rh.views.enviar_email'),
    url(r'^cadastro/', 'mysite.cadastro_rh.views.tela_cadastro'),
    url(r'^login/', 'mysite.cadastro_rh.views.login'),
    url(r'^sair/', 'mysite.cadastro_rh.views.sair'),


    url(r'^admin/', include(admin.site.urls)),
    url(r'.*\.js$', 'mysite.cadastro_rh.views.java_script'),
)
