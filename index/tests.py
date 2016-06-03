#coding: utf-8
from django.test import TestCase

from .forms import *

# Create your tests here.
class RegistroRestauranteTestCase(TestCase):
	def setUp(self):
		self.data = {
			'email': 'wall_tec@hotmail.com', 
			'telefone': '12345678', 
			'nome': 'wallBar2', 
			'cnpj': '12345678',
			'password_a': 'tretass',
			'password_b': 'tretass',
			'tipo_cozinha': 'Variada', 
			'faz_delivery': 'True',
			'nome_completo_responsavel': 'blablabla',
			'email_responsavel': 'bal.todos',
			'telefone_responsavel': '1234567',
			'estado': 'Pará',
			'municipio': 'nem sei',
			'bairro': 'nenhum',
			'rua': 'vixxi',
			'numero': 'puts',
			'complemento': 'nem dá',
			'cep': '12345678',
			'nivel': 'OUTRO'
		}

	def test_registro(self):
		form = Form_Restaurant_Register(self.data)
		if not form.is_valid():
			for v in form.errors:
				print('%s: %s' % (v, form.errors[v]))
		self.assertTrue(form.is_valid())