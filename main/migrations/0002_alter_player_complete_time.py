# Generated by Django 3.2.3 on 2021-05-27 21:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='complete_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 27, 21, 58, 44, 847406, tzinfo=utc)),
        ),
    ]
