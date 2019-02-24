# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MissouriData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('county', models.IntegerField(null=True)),
                ('est_name', models.CharField(max_length=200, null=True)),
                ('est_addr', models.CharField(max_length=500, null=True)),
                ('est_city', models.CharField(max_length=200, null=True)),
                ('est_state', models.CharField(max_length=100, null=True)),
                ('est_zip', models.IntegerField(null=True)),
                ('est_number', models.CharField(max_length=200, null=True)),
                ('app_apr_code', models.CharField(max_length=100, null=True)),
                ('date_lic', models.DateField(null=True)),
            ],
        ),
    ]
