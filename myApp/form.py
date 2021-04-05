from .models import *
from django import forms
from django.forms import ModelChoiceField


class MenuModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s) %s" % (obj.categoryId, obj.categoryName)


class InsertCategory(forms.ModelForm):
    categoryName = forms.CharField(label="Category Name")

    def __init__(self, *args, **kwargs):
        super(InsertCategory, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control bg-light',
            })

    class Meta:
        model = Categories
        exclude = ('categoryId', 'categoryTimeOfCreation')


class InsertTransactions(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(InsertTransactions, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control bg-light',
            })

    class Meta:
        model = Transactions
        exclude = ('transId', 'transBillId', 'transTimeOfCreation')


class InsertItem(forms.ModelForm):
    itemCategoryId = forms.ModelChoiceField(label="Select Category", queryset=Categories.objects.all())
    itemName = forms.CharField(label="Item's Name")
    itemPurchasePrice = forms.FloatField(label="Item's Purchase Price(per kg/unit)")
    itemSellingPrice = forms.FloatField(label="Item's Selling Price(per kg/unit)")
    itemAlertVal = forms.FloatField(label="Enter alert value of item,"
                                          " so you can get red alert if value is below aspect (in kg/unit)")
    itemStock = forms.FloatField(label="Enter total stock of an item (in kg/unit)")

    def __init__(self, *args, **kwargs):
        super(InsertItem, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control bg-light',
            })

    class Meta:
        model = Items
        exclude = ('itemId', 'itemTimeOfCreation')


class InsertKart(forms.ModelForm):
    class Meta:
        model = Karts
        exclude = ('kartId',)
