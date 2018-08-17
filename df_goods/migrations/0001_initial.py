# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('gtitle', models.CharField(max_length=20)),
                ('gpic', models.ImageField(upload_to='df_goods')),
                ('gprice', models.DecimalField(max_digits=5, decimal_places=2)),
                ('isDelete', models.BooleanField(default=False)),
                ('gunit', models.CharField(max_length=20, default='500g')),
                ('gclick', models.IntegerField()),
                ('gabstract', models.CharField(max_length=100)),
                ('grepertory', models.IntegerField()),
                ('gcontent', tinymce.models.HTMLField()),
            ],
            options={
                'db_table': 'goodsinfo',
            },
        ),
        migrations.CreateModel(
            name='TypeInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('ttitle', models.CharField(max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'typeinfo',
            },
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='gtype',
            field=models.ForeignKey(to='df_goods.TypeInfo'),
        ),
    ]
