# Generated by Django 2.0.7 on 2018-07-26 16:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todoapplist', '0005_auto_20180726_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='created',
            field=models.DateField(default=datetime.datetime(2018, 7, 26, 16, 40, 36, 388339, tzinfo=utc)),
        ),
    ]