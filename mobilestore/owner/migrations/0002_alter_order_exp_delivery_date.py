# Generated by Django 3.2.6 on 2021-09-08 10:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='exp_delivery_date',
            field=models.DateField(default=datetime.date(2021, 9, 12), null=True),
        ),
    ]
