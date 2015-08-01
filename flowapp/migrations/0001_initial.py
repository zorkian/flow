# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('api_key', models.CharField(max_length=128)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('accounttype', models.IntegerField(default=1)),
                ('accountstatus', models.IntegerField(default=0)),
            ],
        ),
    ]
