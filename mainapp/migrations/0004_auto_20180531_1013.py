# Generated by Django 2.0.5 on 2018-05-31 14:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20180531_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='sign_in_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 31, 14, 13, 25, 818073, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='member',
            name='sign_out_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 31, 14, 13, 25, 818073, tzinfo=utc)),
        ),
    ]
