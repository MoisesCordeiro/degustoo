# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurante', '0009_auto_20160406_1431'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gerenciadorrestaurante',
            name='cpf',
        ),
        migrations.AddField(
            model_name='restaurante',
            name='faz_delivery',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='restaurante',
            name='tipo_cozinha',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=6, default=0),
            preserve_default=True,
        ),
    ]
