# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-13 17:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArtsUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='用户名')),
                ('password', models.CharField(max_length=80, verbose_name='密码')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('is_active', models.IntegerField(choices=[(0, '未被激活'), (1, '已经激活')], default=0, verbose_name='是否激活')),
                ('createtime', models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='添加时间')),
                ('flag', models.IntegerField(choices=[(0, '未删除'), (1, '已删除')], default=0, verbose_name='控制字段')),
            ],
            options={
                'verbose_name': '会员信息',
                'verbose_name_plural': '会员信息',
                'db_table': 'arts_user',
                'ordering': ['-createtime'],
            },
        ),
    ]