# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-15 13:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goodslist', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goodscomment',
            name='goods',
        ),
        migrations.DeleteModel(
            name='GoodsComment',
        ),
    ]
