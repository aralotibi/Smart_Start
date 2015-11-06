# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20151106_1742'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vote',
            old_name='rewview',
            new_name='review',
        ),
    ]
