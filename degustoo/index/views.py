from django.shortcuts import render


from django.views.generic import View
from django.http import Http404, JsonResponse, HttpResponseBadRequest
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
from .forms import *
from degAuth.models import *
from core.models import *
from restaurante.models import *

import json
import unicodedata

class Index(View):
    template = "index/index.html"
    def get(self, request):
        return render(request, self.template, {})

class Registrar(View):
    template = "index/registrar.html"
    form_class = Form_Registro
    
    def get(self, request):
        form = self.form_class()
        return render(request, self.template, {'form':form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            pass
            # save user on database
        return render(request, self.template, {'form':form})

class RegistroRestaurante(View):
    template = "index/registrar_restaurante.html"
    form_class = Form_Restaurant_Register

    def get(self, request):
        form = self.form_class()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            # send email to Degustoo with the form data
            estado = form.cleaned_data['estado']
            municipio = form.cleaned_data['municipio']
            bairro = form.cleaned_data['bairro']
            rua = form.cleaned_data['rua']
            numero = form.cleaned_data['numero']
            complemento = form.cleaned_data['complemento']
            cep = form.cleaned_data['cep']
            endereco_obj = Endereco.objects.create(
                estado=estado, municipio=municipio, 
                bairro=bairro, rua=rua, numero=numero,
                complemento=complemento, cep=cep)

            nome_resp = form.cleaned_data['nome_completo_responsavel']
            email_resp = form.cleaned_data['email_responsavel']
            tel_resp = form.cleaned_data['telefone_responsavel']
            gerenciador_obj = GerenciadorRestaurante.objects.create(
                email=email_resp, telefone=tel_resp, nome_completo=nome_resp)

            email = form.cleaned_data['email']
            telefone = form.cleaned_data['telefone']
            usuario_obj = Usuario.objects.create_restaurant_user(
                email=email, telefone=telefone, password='blablabla')

            nome = form.cleaned_data['nome']
            cnpj = form.cleaned_data['cnpj']
            tipo_cozinha = form.cleaned_data['tipo_cozinha']
            faz_delivery = form.cleaned_data['faz_delivery']
            restaurante_obj = Restaurante.objects.create(
                usuario=usuario_obj, gerenciador=gerenciador_obj, endereco=endereco_obj,
                nome=nome, cnpj=cnpj, tipo=0,
                tipo_cozinha=tipo_cozinha, faz_delivery=faz_delivery)

            return render(request, self.template, {'form': form})
        else:
            erros = json.dumps(form.errors)
            data = json.dumps(dict([(k, [str(e) for e in v]) for k,v in form.errors.items()]))
            return HttpResponseBadRequest(data, content_type='application/json')
            
class Login(View):
    template = "index/login.html"
    form_class = Form_Login
    
    def get(self, request):
        form = self.form_class()
        return render(request, self.template, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            #log user in
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email,password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # redirect to the right page
                    if user.nivel == 0:
                        return redirect('administracao:index')
                    elif user.nivel == 1:
                        return redirect('cliente:index')
                    elif user.nivel == 2 or user.nivel == 3:
                        return redirect('restaurante:index')
                    else:
                        raise Http404("You are not a valid user")
                else:
                    raise Http404("You are not an active user, check your email account and send us an user confirmation")
        return render(request, self.template, {'form':form})

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect("index:index")