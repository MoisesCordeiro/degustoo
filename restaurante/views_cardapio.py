# -*- coding: UTF-8 -*-
from django.shortcuts import render

# Create your views here.
from core.ajax import *

from django.views.generic import View
from django.http import Http404, JsonResponse, HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404, redirect

from models import *
from mixins import *
from forms import *
from ajaxTables import *

class CriarCardapio(RestauranteMixin, View):
    """
        Cria cardapio via json
    """
    form_class = Form_Cardapio_Default
    
    def post(self, request, **kargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            if not self.restaurante.menuTitleIsFree(form.cleaned_data['titulo']):
                data = prepareAjaxErrorMessage('Menu already exists')
            else:
                cardapio = Cardapio(
                    restaurante=self.restaurante, imagem=form.cleaned_data['imagem'],
                    titulo=form.cleaned_data['titulo'], tipo=form.cleaned_data['tipo'])
                cardapio.save()
    
                #preparar resultado
                cardapios = self.restaurante.getEvery_menu()
                result = buildCardapioTable(cardapios, token=request.COOKIES['csrftoken'])
                data = prepareAjaxSuccessData(result, len(cardapios))
        else:
            #formulario invalido
            data = prepareAjaxErrorMessage('Invalid form')
        return JsonResponse(data)

class CardapioView(RestauranteMixin, CardapioMixin, View):
    template = 'restaurante/cardapio/cardapio.html'
    form_class = Form_Cardapio_Default

    def get(self, request):
        itens = self.cardapio.getEvery_item()
        opcoes = self.cardapio.getEvery_option()
        subcardapios = self.cardapio.getEvery_submenu()
        return render(request, self.template, 
            {'cardapio':self.cardapio, 'itens':itens, 'opcoes':opcoes, 
            'subcardapios':subcardapios})

class ListaCardapio(RestauranteMixin, View):
    """
        Mostra lista de cardapios em template
    """
    template = 'restaurante/cardapio/lista_cardapio.html'
    form_class = Form_Cardapio_Default
    def get(self, request):
        cardapios = self.restaurante.getEvery_menu()
        form = self.form_class()
        return render(request, self.template, {'cardapios':cardapios, 'form':form}) 

class EditarCardapio(RestauranteMixin, CardapioMixin, View):
    """
        Edita cardapio via json
    """
    form_class = Form_Cardapio_Default
    def post(self, request):
        form = self.form_class(request.POST, instance=self.cardapio)
        if form.is_valid():
            #thing = self.restaurante.menuTitleIsUnique(form.cleaned_data['titulo'])
            thing = self.restaurante.cardapio_set.filter(titulo__iexact=form.cleaned_data['titulo'])
            if self.restaurante.menuTitleIsUnique(form.cleaned_data['titulo']):
                form.save()
                cardapios = self.restaurante.getEvery_menu()
                result = buildCardapioTable(cardapios, token=request.COOKIES['csrftoken'])
                data = prepareAjaxSuccessData(result, len(cardapios))
            else:
                #data = prepareAjaxErrorMessage('Menu with this name already exists in this restaurant')
                return HttpResponse(len(thing))
        else:
            data = prepareAjaxErrorMessage('Invalid form')
        return JsonResponse(data)

class DeletarCardapio(RestauranteMixin, CardapioMixin, View):
    """
        Deleta cardapio via json
    """
    form_class = Form_Subcardapio_Delete
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cardapio = Cardapio.objects.get(pk=form.cleaned_data['id'])
            cardapio.delete()
            cardapios = self.restaurante.getEvery_menu()
            result = buildCardapioTable(cardapios, token=request.COOKIES['csrftoken'])
            data = prepareAjaxSuccessData(result, len(cardapios))
        else:
            data = prepareAjaxErrorMessage('Invalid form')
        return JsonResponse(data)

class CriarItem(RestauranteMixin, CardapioMixin, View):
    """
        Cria item via json
    """
    form_class = Form_Item_Default
    def post(self, request, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # prepare data to save
            if self.cardapio.itemNameIsFree(form.cleaned_data['nome']):
                # can save the data, any subcardapio was found
                item = Item(
                    cardapio = self.cardapio, nome=form.cleaned_data['nome'],
                    preco=form.cleaned_data['preco'],ingredientes=form.cleaned_data['ingredientes'])
                item.save()

                # prepare data to send back using json
                itens = self.cardapio.getEvery_item()
                result = buildItemTable(itens, self.cardapio.id, token=request.COOKIES['csrftoken'])
                
                data = prepareAjaxSuccessData(result, len(itens))
            else:
                # there is an object with the same name in the same menu
                data = prepareAjaxErrorMessage('Item already exists inside this menu')
        else:
            data = prepareAjaxErrorMessage('Invalid form')
        return JsonResponse(data)

class EditarItem(RestauranteMixin, CardapioMixin, ItemCardapioMixin, View):
    """
        Edita item de cardapio via json
    """
    form_class = Form_Item_Default

    def post(self, request):
        form = self.form_class(request.POST, instance=self.item)
        if form.is_valid():
            form.save()
            itens = self.cardapio.getEvery_item()
            result = buildItemTable(itens, self.cardapio.id, token=request.COOKIES['csrftoken'])
            data = prepareAjaxSuccessData(result, len(itens))
        return JsonResponse(data)

class DeletarItemCardapio(RestauranteMixin, CardapioMixin, ItemCardapioMixin, View):
    """
        Deleta item de cardapio via json
    """
    form_class = Form_Item_Delete

    def post(self, request):
        form = self.form_class(request.POST) 
        if form.is_valid():
            item = Item.objects.get(pk=form.cleaned_data['id'])
            item.delete()
            itens = self.cardapio.getEvery_item()
            result = buildItemTable(itens, self.cardapio.id, token=request.COOKIES['csrftoken'])
            data = prepareAjaxSuccessData(result, len(itens))
        else:
            data = prepareAjaxErrorMessage('Invalid form')
        return JsonResponse(data)