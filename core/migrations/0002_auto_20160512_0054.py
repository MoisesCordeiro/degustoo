# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_cliente_usuario'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
        ('restaurante', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='voto',
            name='restaurante',
            field=models.ForeignKey(to='restaurante.Restaurante'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='resposta',
            name='comentario',
            field=models.ForeignKey(to='core.Comentario'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='resposta',
            name='sender',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pedido',
            name='cliente',
            field=models.ForeignKey(to='clientes.Cliente'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pedido',
            name='endereco',
            field=models.ForeignKey(to='core.Endereco'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pedido',
            name='restaurante',
            field=models.ForeignKey(to='restaurante.Restaurante'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='itempedido',
            name='itens',
            field=models.ManyToManyField(to='restaurante.Item'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='itempedido',
            name='opcao',
            field=models.ForeignKey(to='restaurante.Opcao'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='itempedido',
            name='pedido',
            field=models.ForeignKey(to='core.Pedido'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='itempedido',
            name='subcardapios',
            field=models.ForeignKey(to='restaurante.Subcardapio'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comentario',
            name='cliente',
            field=models.ForeignKey(to='clientes.Cliente'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comentario',
            name='restaurante',
            field=models.ForeignKey(to='restaurante.Restaurante'),
            preserve_default=True,
        ),
    ]
