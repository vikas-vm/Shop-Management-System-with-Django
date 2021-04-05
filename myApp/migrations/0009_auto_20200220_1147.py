# Generated by Django 3.0.2 on 2020-02-20 06:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0008_auto_20200220_0112'),
    ]

    operations = [
        migrations.AddField(
            model_name='karts',
            name='kartItemPrice',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='bills',
            name='billTimeOfCreation',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 20, 6, 17, 43, 779309, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='categories',
            name='categoryTimeOfCreation',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 20, 6, 17, 43, 779309, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='customers',
            name='customerTimeOfCreation',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 20, 6, 17, 43, 778285, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='items',
            name='itemTimeOfCreation',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 20, 6, 17, 43, 779309, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='payments',
            name='payTimeOfCreation',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 20, 6, 17, 43, 780306, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='solditems',
            name='soldTimeOfCreation',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 20, 6, 17, 43, 780306, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='transTimeOfCreation',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 20, 6, 17, 43, 780306, tzinfo=utc)),
        ),
    ]