# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20151106_2115'),
    ]

    operations = [
        migrations.RenameField(
            model_name='school',
            old_name='title',
            new_name='name',
        ),
    ]
