from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.views import View
from .models import Categories, Items
from django.db.models import Q, Sum
from .form import *
import json
from django.core import serializers
from django.http import JsonResponse, HttpResponse

# Create your views here.


class Index(View):
    template_name = 'base.html'

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name)


def category(r):
    data = {
        'categories': Categories.objects.all(),
        'categoryForm': InsertCategory()
    }
    return render(r, 'category.html', data)


def item(r):
    data = {
        'items': Items.objects.all(),
        'itemForm': InsertItem()
    }
    return render(r, 'createItem.html', data)


def loader(request):
    data = {
        'categories': Categories.objects.all(),
        'items': Items.objects.all().order_by('itemName'),
    }
    if request.is_ajax():
        return render(request, 'index.html', data)
    else:
        return render(request, 'pageNotFound.html')


def kart(request):
    data = {
        'kartItems': Karts.objects.all(),
    }
    return render(request, 'kart.html', data)


def stock(r):
    data = {
        'categories': Categories.objects.all(),
        'items': Items.objects.all().order_by('itemName'),
    }
    return render(r, 'stock.html', data)


def order(r):
    data = {
        'kartItems': Karts.objects.all(),
        'totalPrice': Karts.objects.all().aggregate(Sum('kartItemPrice')),
    }
    return render(r, 'order.html', data)


def bill(r):
    if 'bill_id' in r.session:
        pk = r.session['bill_id']
        data = {
            'soldItems': SoldItems.objects.filter(soldBillId=pk),
            'bill': Bills.objects.get(pk=pk),
        }
        return render(r, 'bill.html', data)
    else:
        return render(r, 'bill.html')


class SaveCategory(View):
    form_class = InsertCategory
    template_name = "index.html"

    def post(self, *args, **kwargs):
        if self.request.is_ajax and self.request.method == "POST":
            form = self.form_class(self.request.POST)
            if form.is_valid():
                instance = form.save()
                ser_instance = serializers.serialize('json', [instance, ])
                return JsonResponse({"instance": ser_instance}, status=200)
            else:
                return JsonResponse({"error": form.errors}, status=400)
        return JsonResponse({"error": ""}, status=400)


class SaveTrans(View):
    form_class = InsertTransactions
    template_name = "transaction.html"

    def get(self, *args, **kwargs):
        form = self.form_class()
        trans = Transactions.objects.all()
        num = 0
        for x in trans:
            if x.transStatus == 0:
                num = num + x.transAmount
            else:
                num = num - x.transAmount

        data = {
            'transactionForm': form,
            'transactions': Transactions.objects.all().order_by('-pk'),
            'totalDeposits': Transactions.objects.filter(transStatus=0).aggregate(Sum('transAmount')),
            'totalWithdraw': Transactions.objects.filter(transStatus=1).aggregate(Sum('transAmount')),
            'currentBalance': num,
        }
        return render(self.request, self.template_name, data)

    def post(self, *args, **kwargs):
        if self.request.is_ajax and self.request.method == "POST":
            form = self.form_class(self.request.POST)
            if form.is_valid():
                instance = form.save()
                ser_instance = serializers.serialize('json', [instance, ])
                return JsonResponse({"instance": ser_instance}, status=200)
            else:
                return JsonResponse({"error": form.errors}, status=400)
        return JsonResponse({"error": ""}, status=400)


class SaveItem(View):
    form_class = InsertItem
    template_name = "index.html"

    def post(self, *args, **kwargs):
        if self.request.is_ajax and self.request.method == "POST":
            form = self.form_class(self.request.POST)
            if form.is_valid():
                instance = form.save()
                ser_instance = serializers.serialize('json', [instance, ])
                return JsonResponse({"instance": ser_instance}, status=200)
            else:
                return JsonResponse({"error": form.errors}, status=400)
        return JsonResponse({"error": ""}, status=400)


class SaveKartItem(View):
    form_class = InsertKart
    template_name = "index.html"

    def post(self, *args, **kwargs):
        if self.request.is_ajax and self.request.method == "POST":
            form = self.form_class(self.request.POST)
            if form.is_valid():
                instance = form.save()
                ser_instance = serializers.serialize('json', [instance, ])
                return JsonResponse({"instance": ser_instance}, status=200)
            else:
                return JsonResponse({"error": form.errors}, status=400)
        return JsonResponse({"error": ""}, status=400)


def delete_kart_item(request):
    if request.is_ajax and request.method == "GET":
        kart_id = request.GET['id']
        Karts.objects.filter(pk=kart_id).delete()
        return HttpResponse("Success!")
    else:
        return HttpResponse("Request method is not a GET")


def reset_kart_item(request):
    if request.is_ajax and request.method == "GET":
        Karts.objects.all().delete()
        return HttpResponse("Success!")
    else:
        return HttpResponse("Request method is not a GET")


def generate_bill(request):
    if request.is_ajax and request.method == "GET":
        name = request.GET['name']
        pay = request.GET['pay']
        payback = request.GET['payback']
        total = request.GET['total']
        time = timezone.now()
        bill = Bills()
        bill.billName = name
        bill.billPayAmount = pay
        bill.billPaybackAmount = payback
        bill.billTotalAmount = total
        bill.billTimeOfCreation = time
        bill.save()

        bill_id = Bills.objects.filter(billTimeOfCreation=time)
        request.session['bill_id'] = bill_id[0].billId
        return HttpResponse("Success!")
    else:
        return HttpResponse("Request method is not a GET")


def add_sold_item(request):
    if request.is_ajax and request.method == "GET":

        kart_items = Karts.objects.all()
        bill_id = request.session['bill_id']
        for x in kart_items:
            sold_item = SoldItems()
            sold_item.soldBillId = Bills(bill_id)
            sold_item.soldItemId = Items(x.kartItemId.itemId)
            sold_item.soldItemVol = x.kartItemVol
            sold_item.soldPrice = x.kartItemPrice
            sold_item.save()
            item_stock = Items.objects.get(pk=x.kartItemId.itemId)
            stock_vol = item_stock.itemStock
            item_stock.itemStock = (stock_vol - x.kartItemVol)
            item_stock.save()

        bill_data = Bills.objects.get(pk=bill_id)
        trans = Transactions()
        trans.transBillId = bill_data
        trans.transStatus = 0
        trans.transAmount = bill_data.billPayAmount
        trans.save()
        trans.transBillId = bill_data
        trans.transStatus = 1
        trans.transAmount = bill_data.billPaybackAmount
        trans.save()
        Karts.objects.all().delete()
        return HttpResponse("Success!")
    else:
        return HttpResponse("Request method is not a GET")
