# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-06 14:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='question_tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('content', models.TextField()),
                ('difficulty', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='submissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField()),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ctracker.questions')),
            ],
        ),
        migrations.CreateModel(
            name='tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=60)),
                ('first_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=80)),
                ('password_salt', models.CharField(max_length=80)),
                ('active', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='submissions',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ctracker.users'),
        ),
        migrations.AddField(
            model_name='questions',
            name='author_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ctracker.users'),
        ),
        migrations.AddField(
            model_name='question_tags',
            name='question_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ctracker.questions'),
        ),
        migrations.AddField(
            model_name='question_tags',
            name='tag_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ctracker.tags'),
        ),
    ]