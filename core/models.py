from django.db import models
from django.conf import settings
# Create your models here.

from clientes.models import Cliente
from restaurante.models import Restaurante

class Endereco(models.Model):
    estado = models.CharField(max_length=50)
    municipio = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50) 
    rua = models.CharField(max_length=50)
    numero = models.CharField(max_length=50) 
    complemento = models.CharField(max_length=50) 
    cep = models.CharField(max_length=50)

    def __unicode__(self):
        return self.cep
    
class Voto(models.Model):
    KIND = (
            (0, "-"),
            (1, "+"),
    )
    
    QUANTITY = (
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
    )

    cliente = models.ForeignKey(Cliente)
    restaurante = models.ForeignKey(Restaurante)
    tipo = models.IntegerField(choices=KIND)
    quantidade = models.IntegerField(choices=QUANTITY)

    def __unicode__(self):
        return self.quantidade
    
class Comentario(models.Model):
    cliente = models.ForeignKey(Cliente)
    restaurante = models.ForeignKey(Restaurante)
    texto = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.texto

class Resposta(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL)
    comentario = models.ForeignKey(Comentario)
    texto = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.texto

class Pedido(models.Model):
    PAYMENT= (
        (0, "Credit Card"),
        (1, "Entrega"),
    )

    WITHDRAW = (
        (0, "Pegar no caixa"),
        (1, "Delivery"),
    )

    STATUS = (
        (0, "Enviando"),
        (1, "Preparando"),
        (2, "Entregando"),
        (3, "Estornado"),
        (4, "Entregue"),
    )

    cliente = models.ForeignKey(Cliente)
    restaurante = models.ForeignKey(Restaurante)
    observacao = models.CharField(max_length=500, blank=True)
    forma_pagamento = models.IntegerField(choices=PAYMENT)
    forma_retirada = models.IntegerField(choices=WITHDRAW)
    status = models.IntegerField(choices=STATUS)
    troco_para = models.DecimalField(max_digits=6, decimal_places=6, default=0, blank=True)
    total = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    data_envio = models.DateTimeField(auto_now_add=True)

    def get_payment_method(self):
        pass

    def get_withdraw_method(self):
        pass

    def get_status(self):
        pass

    def set_status(self, status):
        pass

    def get_change(self):
        pass

    def generate_total_price(self):
        pass

class Item_Pedido(models.Model):
    # pedido = models.foreignKey(Pedido)
    # itens = models.ManyToManyField("restaurante.Item")
    # opcao = models.One
    # subcardapios 
    # combo 
    # promocao 
    # preco 
    pass
