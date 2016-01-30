# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_Post',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('date_created', models.DateTimeField(auto_created=True)),
                ('title', models.CharField(max_length=140)),
                ('blog_code', models.TextField()),
            ],
        ),
    ]
