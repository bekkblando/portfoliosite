# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_post',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
