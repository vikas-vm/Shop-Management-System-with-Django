# Generated by Django 3.0.2 on 2020-02-20 06:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0010_auto_20200220_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bills',
            name='billTimeOfCreation',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 20, 6, 42, 23, 69980, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='categories',
            name='categoryTimeOfCreation',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 20, 6, 42, 23, 69980, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='customers',
            name='customerTimeOfCreation',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 20, 6, 42, 23, 69980, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='items',
            name='itemTimeOfCreation',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 20, 6, 42, 23, 69980, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='payments',
            name='payTimeOfCreation',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 20, 6, 42, 23, 69980, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='solditems',
            name='soldTimeOfCreation',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 20, 6, 42, 23, 69980, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='transTimeOfCreation',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 20, 6, 42, 23, 69980, tzinfo=utc)),
        ),
    ]