# Generated by Django 2.0.2 on 2020-01-24 08:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('photoapp', '0012_auto_20200124_0710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 24, 8, 8, 13, 186516, tzinfo=utc)),
        ),
    ]
