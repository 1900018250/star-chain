# Generated by Django 2.0.6 on 2018-06-10 15:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mining', '0003_auto_20180610_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mining',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 10, 15, 15, 25, 90406), verbose_name='添加时间'),
        ),
    ]
