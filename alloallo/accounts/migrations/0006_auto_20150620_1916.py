# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20150620_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bt_customer_id',
            field=models.IntegerField(null=True),
        ),
    ]
