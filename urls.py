from django.conf.urls import url
from . import views

urlpatterns = [
	url('api/add_bill/', views.add_bill, name='add-bill'),
	url('api/split_bill/', views.split_bill, name='split-bill'),
	url('api/mark_amount_paid/', views.mark_amount_paid, name='mark-amount-paid'),
	url('api/mark_bill_paid/', views.mark_bill_paid, name='mark-bill-paid'),
	url('api/mark_bill_unpaid/', views.mark_bill_unpaid, name='mark-bill-paid'),
	url('api/delete_bill/', views.delete_bill, name='delete-bill'),
	url(r'^$', views.index, name='bill-index'),
]