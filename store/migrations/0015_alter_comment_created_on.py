# Generated by Django 4.0.1 on 2022-02-17 15:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_auto_20210203_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 17, 20, 17, 11, 426001)),
        ),
    ]
