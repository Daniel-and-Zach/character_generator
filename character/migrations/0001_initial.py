# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Core',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=100)),
                ('back_story', models.TextField()),
                ('height', models.CharField(max_length=50)),
                ('weight', models.FloatField()),
                ('strength', models.IntegerField()),
                ('wisdom', models.IntegerField()),
                ('constitution', models.IntegerField()),
                ('dexterity', models.IntegerField()),
                ('intelligence', models.IntegerField()),
                ('charisma', models.IntegerField()),
            ],
        ),
    ]
