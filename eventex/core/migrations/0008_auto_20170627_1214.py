# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-27 12:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_course'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Course',
            new_name='CourseOld',
        ),
        migrations.AlterModelOptions(
            name='courseold',
            options={'verbose_name': 'Curso', 'verbose_name_plural': 'Cursos'},
        ),
    ]