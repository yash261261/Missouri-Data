# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='missouridata',
            name='date_lic',
            field=models.DateField(null=True, blank=True),
        ),
    ]
