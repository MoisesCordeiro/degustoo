# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cardapio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imagem', models.ImageField(null=True, upload_to=b'menu_images/', blank=True)),
                ('titulo', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GerenciadorRestaurante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=75)),
                ('telefone', models.CharField(max_length=50)),
                ('nome_completo', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50)),
                ('preco', models.DecimalField(default=0, max_digits=6, decimal_places=2)),
                ('ingredientes', models.CharField(max_length=255, blank=True)),
                ('cardapio', models.ForeignKey(blank=True, to='restaurante.Cardapio', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Opcao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rotulo', models.CharField(max_length=50)),
                ('cardapio', models.ForeignKey(to='restaurante.Cardapio')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Restaurante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50)),
                ('cnpj', models.CharField(max_length=50)),
                ('imagem', models.ImageField(upload_to=b'restaurant_profile', null=True, verbose_name=b'Logo Restaurante', blank=True)),
                ('tipo', models.IntegerField(choices=[(0, b'Comum'), (1, b'Diamante')])),
                ('tipo_cozinha', models.CharField(max_length=100, blank=True)),
                ('faz_delivery', models.BooleanField(default=False)),
                ('endereco', models.OneToOneField(to='core.Endereco')),
                ('gerenciador', models.OneToOneField(to='restaurante.GerenciadorRestaurante')),
                ('usuario', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subcardapio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=50)),
                ('cardapio', models.ForeignKey(to='restaurante.Cardapio')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='item',
            name='opcao',
            field=models.ForeignKey(blank=True, to='restaurante.Opcao', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='sub_cardapio',
            field=models.ForeignKey(blank=True, to='restaurante.Subcardapio', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cardapio',
            name='restaurante',
            field=models.ForeignKey(to='restaurante.Restaurante'),
            preserve_default=True,
        ),
    ]
