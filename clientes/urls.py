from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views.cliente import HomeCliente, MeusDados

urlpatterns = [
    # Examples:
    # url(r'^$', 'Degustoo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', HomeCliente.as_view(), name="index"),
    url(r'^meus-dados/$', MeusDados.as_view(), name="meus_dados"),
]