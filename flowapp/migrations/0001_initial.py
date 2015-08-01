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
                ('name', models.CharField(unique=True, max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('api_key', models.CharField(max_length=128)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('accounttype', models.IntegerField(default=1)),
                ('accountstatus', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('author', models.ForeignKey(to='flowapp.Account', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('parent', models.ForeignKey(blank=True, to='flowapp.Topic', null=True)),
                ('tags', models.ManyToManyField(to='flowapp.Tag')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='tags',
            field=models.ManyToManyField(to='flowapp.Tag'),
        ),
        migrations.AddField(
            model_name='event',
            name='topic',
            field=models.ForeignKey(to='flowapp.Topic'),
        ),
        migrations.AddField(
            model_name='account',
            name='topic',
            field=models.ForeignKey(to='flowapp.Topic'),
        ),
    ]
