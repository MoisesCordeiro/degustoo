# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('texto', models.TextField()),
                ('data_envio', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estado', models.CharField(max_length=50)),
                ('municipio', models.CharField(max_length=50)),
                ('bairro', models.CharField(max_length=50)),
                ('rua', models.CharField(max_length=50)),
                ('numero', models.CharField(max_length=50)),
                ('complemento', models.CharField(max_length=50, blank=True)),
                ('cep', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Itempedido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('preco', models.DecimalField(default=0, max_digits=6, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('observacao', models.CharField(max_length=500, blank=True)),
                ('forma_pagamento', models.IntegerField(choices=[(0, b'Credit Card'), (1, b'Entrega')])),
                ('forma_retirada', models.IntegerField(choices=[(0, b'Pegar no caixa'), (1, b'Delivery')])),
                ('status', models.IntegerField(choices=[(0, b'Enviando'), (1, b'Preparando'), (2, b'Entregando'), (3, b'Estornado'), (4, b'Entregue')])),
                ('troco_para', models.DecimalField(default=0, max_digits=6, decimal_places=6, blank=True)),
                ('total', models.DecimalField(default=0, max_digits=6, decimal_places=2)),
                ('data_envio', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('texto', models.TextField()),
                ('data_envio', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Voto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.IntegerField(choices=[(0, b'-'), (1, b'+')])),
                ('quantidade', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('cliente', models.ForeignKey(to='clientes.Cliente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
