# Generated by Django 3.0.2 on 2020-02-20 08:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0011_auto_20200220_1212'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customers',
        ),
        migrations.RemoveField(
            model_name='bills',
            name='billCustomerId',
        ),
        migrations.AddField(
            model_name='bills',
            name='billName',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='bills',
            name='billPayAmount',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='bills',
            name='billPaybackAmount',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='bills',
            name='billTotalAmount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='bills',
            name='billTimeOfCreation',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 20, 8, 11, 17, 896933, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='categories',
            name='categoryTimeOfCreation',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 20, 8, 11, 17, 896933, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='items',
            name='itemTimeOfCreation',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 20, 8, 11, 17, 896933, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='payments',
            name='payTimeOfCreation',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 20, 8, 11, 17, 896933, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='solditems',
            name='soldTimeOfCreation',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 20, 8, 11, 17, 896933, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='transTimeOfCreation',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 20, 8, 11, 17, 896933, tzinfo=utc)),
        ),
    ]
