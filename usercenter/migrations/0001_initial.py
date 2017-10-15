# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-15 13:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddrInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aProvince', models.CharField(max_length=15)),
                ('aCity', models.CharField(max_length=15)),
                ('aDis', models.CharField(blank=True, max_length=15, null=True)),
                ('aAddressee', models.CharField(max_length=20)),
                ('aDetaAddr', models.CharField(max_length=30)),
                ('aPostCode', models.CharField(blank=True, max_length=10, null=True)),
                ('aPhoneNumber', models.CharField(max_length=15)),
                ('isDelete', models.BooleanField(default=False)),
                ('aDefaultAddr', models.BooleanField(default=False)),
                ('extra', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'addrinfo',
            },
        ),
        migrations.CreateModel(
            name='AreaInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aTitle', models.CharField(max_length=20)),
                ('aParent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usercenter.AreaInfo')),
            ],
            options={
                'db_table': 'areainfo',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uName', models.CharField(max_length=30)),
                ('uPassword', models.CharField(max_length=40)),
                ('uEmail', models.CharField(max_length=30)),
                ('uPhoneNumber', models.CharField(max_length=15, null=True)),
                ('uAddr', models.CharField(blank=True, max_length=50, null=True)),
                ('uRegDate', models.DateTimeField()),
                ('isDelete', models.BooleanField(default=False)),
                ('extra', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'userinfo',
            },
        ),
        migrations.AddField(
            model_name='addrinfo',
            name='aUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usercenter.UserInfo'),
        ),
    ]
