# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-10-17 03:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='名称')),
                ('describe', models.TextField(default='', verbose_name='描述')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='更新时间')),
            ],
            options={
                'db_table': 'module',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='名称')),
                ('describe', models.TextField(default='', verbose_name='描述')),
                ('status', models.BooleanField(default=True, verbose_name='状态：')),
                ('update_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='更新时间')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
            ],
            options={
                'db_table': 'project',
            },
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_name', models.CharField(max_length=50, verbose_name='用例名称')),
                ('url', models.TextField(verbose_name='请求URL')),
                ('method', models.IntegerField(verbose_name='请求方法')),
                ('header', models.TextField(verbose_name='请求头')),
                ('parameter_type', models.IntegerField(verbose_name='参数类型')),
                ('parameter_body', models.TextField(verbose_name='参数内容')),
                ('result', models.TextField(verbose_name='结果')),
                ('assert_type', models.IntegerField(verbose_name='断```````````````````言类型')),
                ('assert_text', models.TextField(verbose_name='断言结果')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('status', models.BooleanField(default=True, verbose_name='状态')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.Module')),
            ],
            options={
                'db_table': 'testcase',
            },
        ),
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='名称')),
                ('error', models.IntegerField(verbose_name='错误用例')),
                ('failure', models.IntegerField(verbose_name='失败用例')),
                ('skipped', models.IntegerField(verbose_name='跳过用例')),
                ('tests', models.IntegerField(verbose_name='总用例数')),
                ('run_time', models.FloatField(verbose_name='运行时长')),
                ('result', models.TextField(default='', verbose_name='详细')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
            ],
            options={
                'db_table': 'testresult',
            },
        ),
        migrations.CreateModel(
            name='TestTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='名称')),
                ('describe', models.TextField(default='', verbose_name='描述')),
                ('status', models.IntegerField(default=0, verbose_name='状态：')),
                ('cases', models.TextField(default='', verbose_name='关联用例')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
            ],
            options={
                'db_table': 'testtask',
            },
        ),
        migrations.AddField(
            model_name='testresult',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.TestTask'),
        ),
        migrations.AddField(
            model_name='module',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.Project'),
        ),
    ]
