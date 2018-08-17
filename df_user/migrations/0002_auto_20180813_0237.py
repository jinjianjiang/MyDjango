# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='u_address',
            field=models.CharField(max_length=100, default=''),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='u_delivery',
            field=models.CharField(max_length=50, default=''),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='u_phone',
            field=models.CharField(max_length=11, default=''),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='u_post',
            field=models.CharField(max_length=6, default=''),
        ),
    ]
