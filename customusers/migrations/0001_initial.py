# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('first_name', models.CharField(max_length=30, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last Name')),
                ('user_handle', models.CharField(help_text='Required. 20 characters of less. Only alphanumeric characters and the (+/-/./_) characters', max_length=20, unique=True, error_messages={b'unique': 'A user with that username already exists'}, validators=[django.core.validators.RegexValidator(b'^[\\w.+-]+$', 'Enter a valid username. It may only contain alphanumeric and the (+/-/./_)', b'invalid')])),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name='Email Address')),
                ('profile_pic', models.FileField(upload_to=b'', null=True, verbose_name='Profile Picture')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
