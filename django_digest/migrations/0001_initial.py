# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PartialDigest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('login', models.CharField(max_length=75, db_index=True)),
                ('partial_digest', models.CharField(max_length=100)),
                ('confirmed', models.BooleanField(default=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserNonce',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nonce', models.CharField(unique=True, max_length=100, db_index=True)),
                ('count', models.IntegerField(null=True)),
                ('last_used_at', models.DateTimeField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('last_used_at',),
            },
        ),
    ]
