# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-15 13:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goodsName', models.CharField(max_length=30)),
                ('goodsDesc', models.CharField(max_length=80)),
                ('goodsPrice', models.DecimalField(decimal_places=2, max_digits=7)),
                ('goodsDetail', tinymce.models.HTMLField()),
                ('imgPath', models.ImageField(upload_to='uploads/')),
                ('saleCount', models.IntegerField(default=0)),
                ('gPubdate', models.DateTimeField()),
                ('extra', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'goods',
            },
        ),
        migrations.CreateModel(
            name='GoodsComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=30)),
                ('commentDate', models.DateTimeField()),
                ('comment', tinymce.models.HTMLField()),
                ('extra', models.CharField(blank=True, max_length=20, null=True)),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goodslist.Goods')),
            ],
            options={
                'db_table': 'goodscomment',
            },
        ),
        migrations.CreateModel(
            name='GoodSort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sortName', models.CharField(max_length=10)),
                ('sortPic', models.ImageField(upload_to='uploads/')),
                ('sortClass', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'goodsort',
            },
        ),
        migrations.AddField(
            model_name='goods',
            name='goodSort',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goodslist.GoodSort'),
        ),
    ]
