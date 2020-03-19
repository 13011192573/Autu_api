# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-10-17 04:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='module',
            name='project',
        ),
        migrations.RemoveField(
            model_name='testcase',
            name='module',
        ),
        migrations.RemoveField(
            model_name='testresult',
            name='task',
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.IntegerField(default=0, verbose_name='状态：'),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='assert_type',
            field=models.IntegerField(verbose_name='断言类型'),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='status',
            field=models.IntegerField(default=0, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='run_time',
            field=models.IntegerField(verbose_name='运行时长'),
        ),
    ]
