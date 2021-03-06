# Generated by Django 3.0.2 on 2020-02-19 10:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0005_auto_20200219_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bills',
            name='billTimeOfCreation',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 19, 10, 23, 3, 495733, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='categories',
            name='categoryRoot',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='categories',
            name='categoryTimeOfCreation',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 19, 10, 23, 3, 494708, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='customers',
            name='customerTimeOfCreation',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 19, 10, 23, 3, 494708, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='items',
            name='itemTimeOfCreation',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 19, 10, 23, 3, 495733, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='karts',
            name='kartItemId',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='payments',
            name='payTimeOfCreation',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 19, 10, 23, 3, 495733, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='solditems',
            name='soldTimeOfCreation',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 19, 10, 23, 3, 495733, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='transTimeOfCreation',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 19, 10, 23, 3, 495733, tzinfo=utc)),
        ),
    ]
