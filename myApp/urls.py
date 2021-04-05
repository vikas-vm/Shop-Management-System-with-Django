from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name="home"),
    path('category', views.category, name="category"),
    path('item', views.item, name="item"),
    path('loader', views.loader, name="loader"),
    path('kart', views.kart, name="kart"),
    path('stock', views.stock, name="stock"),
    path('order', views.order, name="order"),
    path('bill', views.bill, name="bill"),
    path('transactions', views.SaveTrans.as_view(), name="transactions"),
    path('category_save', views.SaveCategory.as_view(), name="save_category"),
    path('category_item', views.SaveItem.as_view(), name="save_item"),
    path('save_kartItem', views.SaveKartItem.as_view(), name="save_kartItem"),
    path('delete_kartItem', views.delete_kart_item, name="delete_kartItem"),
    path('generate_bill', views.generate_bill, name="generate_bill"),
    path('add_sold_item', views.add_sold_item, name="add_sold_item"),
    path('reset_kartItem', views.reset_kart_item, name="reset_kartItem"),
]
