# Generated by Django 3.0.2 on 2020-02-19 02:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_auto_20200219_0726'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Categories',
        ),
        migrations.DeleteModel(
            name='Customers',
        ),
        migrations.RemoveField(
            model_name='karts',
            name='kartItemId',
        ),
        migrations.RemoveField(
            model_name='payments',
            name='payBillId',
        ),
        migrations.RemoveField(
            model_name='solditems',
            name='soldBillId',
        ),
        migrations.RemoveField(
            model_name='solditems',
            name='soldItemId',
        ),
        migrations.DeleteModel(
            name='Transactions',
        ),
        migrations.DeleteModel(
            name='Bills',
        ),
        migrations.DeleteModel(
            name='Items',
        ),
        migrations.DeleteModel(
            name='Karts',
        ),
        migrations.DeleteModel(
            name='Payments',
        ),
        migrations.DeleteModel(
            name='SoldItems',
        ),
    ]
