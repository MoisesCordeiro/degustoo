#coding: utf-8
from django.shortcuts import render

from django.core.urlresolvers import reverse as r, reverse_lazy
from django.views.generic import View, UpdateView
from django.http import Http404, JsonResponse
from django.shortcuts import render, render_to_response, get_object_or_404, redirect


from clientes.models import Cliente
from clientes.forms import MeusDadosForm

from braces.views import GroupRequiredMixin

class ClienteMixin(object):
    user = None
    def dispatch(self, request, *args, **kwargs):
        try:
            user = request.user
            if user.is_client:
                self.user = user
            else:
                raise Http404("User has not permission to visit this page")
        except Exception:
            raise Http404("User has not permission to visit this page")
        return super(ClienteMixin, self).dispatch(request, *args, **kwargs)

class HomeCliente(GroupRequiredMixin, View):
    template = 'clientes/index.html'
    group_required = ['Cliente']

    def get(self, request):
        return render(request, self.template)

class MeusDados(GroupRequiredMixin, UpdateView):
    form_class = MeusDadosForm
    template_name = 'clientes/meus_dados.html'
    group_required = ['Cliente']
    success_url = reverse_lazy('clientes:index')

    def get_object(self):
        return self.request.user.cliente