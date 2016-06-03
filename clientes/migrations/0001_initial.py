# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=30)),
                ('sobrenome', models.CharField(max_length=30)),
                ('imagem', models.ImageField(upload_to=b'user_profile/', null=True, verbose_name=b'Foto Perfil', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
