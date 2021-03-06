# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-11 13:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=50, verbose_name='主机')),
                ('ip', models.GenericIPAddressField(verbose_name='IP')),
                ('osversion', models.CharField(max_length=50, verbose_name='系统版本')),
                ('memory', models.CharField(max_length=50, verbose_name='内存')),
                ('disk', models.CharField(max_length=50, verbose_name='硬盘')),
                ('vendor_id', models.CharField(max_length=50, verbose_name='供应商')),
                ('model_name', models.CharField(max_length=50, verbose_name='型号')),
                ('cpu_core', models.CharField(max_length=50, verbose_name='CPU')),
                ('product', models.CharField(max_length=50, verbose_name='产品线')),
                ('Manufacturer', models.CharField(max_length=50, verbose_name='制造商')),
                ('sn', models.CharField(max_length=50, verbose_name='SN')),
            ],
            options={
                'verbose_name': '服务器',
                'verbose_name_plural': '服务器',
                'db_table': 'Host',
            },
        ),
    ]
