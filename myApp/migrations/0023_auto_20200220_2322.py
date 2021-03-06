# Generated by Django 3.0.2 on 2020-02-20 17:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0022_auto_20200220_2206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categories',
            name='categoryRoot',
        ),
        migrations.AlterField(
            model_name='bills',
            name='billTimeOfCreation',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 20, 17, 52, 29, 791909, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='categories',
            name='categoryTimeOfCreation',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 20, 17, 52, 29, 791909, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='items',
            name='itemTimeOfCreation',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 20, 17, 52, 29, 791909, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='solditems',
            name='soldTimeOfCreation',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 20, 17, 52, 29, 791909, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='transTimeOfCreation',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 20, 17, 52, 29, 791909, tzinfo=utc)),
        ),
    ]
