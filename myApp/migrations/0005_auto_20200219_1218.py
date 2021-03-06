# Generated by Django 3.0.2 on 2020-02-19 06:48

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0004_bills_categories_customers_items_karts_payments_solditems_transactions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bills',
            name='billTimeOfCreation',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 19, 6, 48, 10, 306991, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='categories',
            name='categoryTimeOfCreation',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 19, 6, 48, 10, 306991, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='customers',
            name='customerTimeOfCreation',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 19, 6, 48, 10, 306991, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='items',
            name='itemCategoryId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.Categories'),
        ),
        migrations.AlterField(
            model_name='items',
            name='itemTimeOfCreation',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 19, 6, 48, 10, 306991, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='payments',
            name='payTimeOfCreation',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 19, 6, 48, 10, 306991, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='solditems',
            name='soldTimeOfCreation',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 19, 6, 48, 10, 306991, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='transTimeOfCreation',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 19, 6, 48, 10, 306991, tzinfo=utc)),
        ),
    ]
