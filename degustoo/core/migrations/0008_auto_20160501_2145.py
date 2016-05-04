# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurante', '0009_auto_20160406_1431'),
        ('core', '0007_auto_20160430_1531'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemPedido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('preco', models.DecimalField(default=0, max_digits=6, decimal_places=2)),
                ('itens', models.ManyToManyField(to='restaurante.Item')),
                ('opcao', models.ForeignKey(to='restaurante.Opcao')),
                ('pedido', models.ForeignKey(to='core.Pedido')),
                ('subcardapios', models.ForeignKey(to='restaurante.Subcardapio')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='item_pedido',
            name='itens',
        ),
        migrations.RemoveField(
            model_name='item_pedido',
            name='opcao',
        ),
        migrations.RemoveField(
            model_name='item_pedido',
            name='pedido',
        ),
        migrations.RemoveField(
            model_name='item_pedido',
            name='subcardapios',
        ),
        migrations.DeleteModel(
            name='Item_Pedido',
        ),
    ]
