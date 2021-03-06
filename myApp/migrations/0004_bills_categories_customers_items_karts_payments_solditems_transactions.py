# Generated by Django 3.0.2 on 2020-02-19 02:15

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myApp', '0003_auto_20200219_0745'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bills',
            fields=[
                ('billId', models.IntegerField(primary_key=True, serialize=False)),
                ('billCustomerId', models.IntegerField()),
                ('billTimeOfCreation', models.DateTimeField(default=datetime.datetime(2020, 2, 19, 2, 15, 52, 749425, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('categoryId', models.IntegerField(primary_key=True, serialize=False)),
                ('categoryName', models.CharField(max_length=50, unique=True)),
                ('categoryRoot', models.IntegerField(default=0, max_length=50, null=True)),
                ('categoryTimeOfCreation', models.DateTimeField(default=datetime.datetime(2020, 2, 19, 2, 15, 52, 749425, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('customerId', models.IntegerField(primary_key=True, serialize=False)),
                ('customerName', models.CharField(max_length=50, null=True)),
                ('customerPhone', models.IntegerField()),
                ('customerAddress', models.TextField(null=True)),
                ('customerEmail', models.EmailField(max_length=254, null=True)),
                ('customerTimeOfCreation', models.DateTimeField(default=datetime.datetime(2020, 2, 19, 2, 15, 52, 749425, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('itemId', models.IntegerField(primary_key=True, serialize=False)),
                ('itemCategoryId', models.IntegerField(default=0)),
                ('itemName', models.CharField(max_length=50)),
                ('itemStatus', models.IntegerField(choices=[(0, 'ByMass'), (1, 'ByWeight')], default=0)),
                ('itemStock', models.FloatField()),
                ('itemAlertVal', models.FloatField()),
                ('itemPurchasePrice', models.FloatField()),
                ('itemSellingPrice', models.FloatField()),
                ('itemTimeOfCreation', models.DateTimeField(default=datetime.datetime(2020, 2, 19, 2, 15, 52, 749425, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('transId', models.IntegerField(primary_key=True, serialize=False)),
                ('transStatement', models.TextField()),
                ('transStatus', models.IntegerField()),
                ('transBillId', models.IntegerField(null=True)),
                ('transAmount', models.IntegerField()),
                ('transTimeOfCreation', models.DateTimeField(default=datetime.datetime(2020, 2, 19, 2, 15, 52, 749425, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='SoldItems',
            fields=[
                ('soldId', models.IntegerField(primary_key=True, serialize=False)),
                ('soldItemVol', models.FloatField()),
                ('soldPrice', models.FloatField()),
                ('soldTimeOfCreation', models.DateTimeField(default=datetime.datetime(2020, 2, 19, 2, 15, 52, 749425, tzinfo=utc))),
                ('soldBillId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.Bills')),
                ('soldItemId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.Items')),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('paymentId', models.IntegerField(primary_key=True, serialize=False)),
                ('payTotal', models.IntegerField()),
                ('paymentGot', models.IntegerField()),
                ('payBack', models.IntegerField()),
                ('payTimeOfCreation', models.DateTimeField(default=datetime.datetime(2020, 2, 19, 2, 15, 52, 749425, tzinfo=utc))),
                ('payBillId', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myApp.Bills')),
            ],
        ),
        migrations.CreateModel(
            name='Karts',
            fields=[
                ('kartId', models.IntegerField(primary_key=True, serialize=False)),
                ('kartItemVol', models.FloatField()),
                ('kartItemId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.Items')),
            ],
        ),
    ]
