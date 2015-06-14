# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, choices=[(b'Elf', b'Elf'), (b'Dwarf', b'Dwarf'), (b'Gnome', b'Gnome'), (b'Half-Elf', b'Half-Elf'), (b'Halfling', b'Halfling'), (b'Half-Orc', b'Half-Orc'), (b'Human', b'Human')])),
                ('size', models.CharField(max_length=255)),
                ('base_speed', models.IntegerField()),
                ('description', models.TextField()),
                ('history', models.TextField()),
            ],
        ),
    ]
