from django.db.models import Model, IntegerField, TextField, CharField, DateTimeField, FloatField,\
    CASCADE, ForeignKey, DO_NOTHING
from django.utils import timezone


class Categories(Model):
    categoryId = IntegerField(primary_key=True)
    categoryName = CharField(max_length=50, unique=True)
    categoryTimeOfCreation = DateTimeField(default=timezone.now())

    def __str__(self):
        return self.categoryName


class Items(Model):
    itemId = IntegerField(primary_key=True)
    itemCategoryId = ForeignKey(Categories, on_delete=CASCADE)
    itemName = CharField(max_length=50)
    itemStatus = IntegerField(default=0, choices=[(0, "ByMass"), (1, "ByUnit")])
    itemStock = FloatField()
    itemAlertVal = FloatField()
    itemPurchasePrice = FloatField()
    itemSellingPrice = FloatField()
    itemTimeOfCreation = DateTimeField(default=timezone.now())


class Bills(Model):
    billId = IntegerField(primary_key=True)
    billName = CharField(max_length=50, null=True)
    billTotalAmount = IntegerField(null=True)
    billPayAmount = IntegerField(null=True)
    billPaybackAmount = IntegerField(null=True)
    billTimeOfCreation = DateTimeField(default=timezone.now())


class SoldItems(Model):
    soldId = IntegerField(primary_key=True)
    soldBillId = ForeignKey(Bills, on_delete=CASCADE)
    soldItemId = ForeignKey(Items, on_delete=CASCADE)
    soldItemVol = FloatField()
    soldPrice = IntegerField()
    soldTimeOfCreation = DateTimeField(default=timezone.now())


class Transactions(Model):
    transId = IntegerField(primary_key=True)
    transStatement = TextField(null=True)
    transStatus = IntegerField(default=0, choices=[(0, "deposit"), (1, "withdraw")])
    transBillId = ForeignKey(Bills, on_delete=DO_NOTHING, null=True)
    transAmount = IntegerField()
    transTimeOfCreation = DateTimeField(default=timezone.now())


class Karts(Model):
    kartId = IntegerField(primary_key=True)
    kartItemId = ForeignKey(Items, on_delete=CASCADE)
    kartItemVol = FloatField()
    kartItemPrice = IntegerField()
