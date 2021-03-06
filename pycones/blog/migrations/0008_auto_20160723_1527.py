# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-23 13:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20160619_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='_content_ca_rendered',
            field=models.TextField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='_content_en_rendered',
            field=models.TextField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='_content_es_rendered',
            field=models.TextField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='_content_eu_rendered',
            field=models.TextField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='_content_gl_rendered',
            field=models.TextField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='content_ca_markup_type',
            field=models.CharField(choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default='markdown', max_length=30),
        ),
        migrations.AlterField(
            model_name='post',
            name='content_en_markup_type',
            field=models.CharField(choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default='markdown', max_length=30),
        ),
        migrations.AlterField(
            model_name='post',
            name='content_es_markup_type',
            field=models.CharField(choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default='markdown', max_length=30),
        ),
        migrations.AlterField(
            model_name='post',
            name='content_eu_markup_type',
            field=models.CharField(choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default='markdown', max_length=30),
        ),
        migrations.AlterField(
            model_name='post',
            name='content_gl_markup_type',
            field=models.CharField(choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default='markdown', max_length=30),
        ),
        migrations.AlterField(
            model_name='post',
            name='content_markup_type',
            field=models.CharField(choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default='markdown', max_length=30),
        ),
    ]
