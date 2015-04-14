# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True)),
                ('scientific_name', models.CharField(null=True, blank=True, max_length=60, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('animal', models.ForeignKey(to='animals.Animal')),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('birthday', models.DateField()),
                ('breed', models.ForeignKey(to='animals.Breed')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='breed',
            unique_together=set([('name', 'animal')]),
        ),
    ]
