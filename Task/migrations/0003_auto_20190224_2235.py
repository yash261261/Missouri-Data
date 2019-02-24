# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0002_auto_20190224_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='missouridata',
            name='date_lic',
            field=models.DateField(null=True),
        ),
    ]
