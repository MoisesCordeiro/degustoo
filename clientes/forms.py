#coding: utf-8

from django import forms

from clientes.models import Cliente



class MeusDadosForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ['nome','sobrenome']
