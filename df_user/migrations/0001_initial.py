# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('u_name', models.CharField(max_length=20)),
                ('u_pwd', models.CharField(max_length=40)),
                ('u_email', models.CharField(max_length=30)),
                ('u_delivery', models.CharField(max_length=50)),
                ('u_address', models.CharField(max_length=100)),
                ('u_post', models.CharField(max_length=6)),
                ('u_phone', models.CharField(max_length=11)),
            ],
            options={
                'db_table': 'userinfo',
            },
        ),
    ]
