from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Max
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils import timezone
from django.http import JsonResponse
import json
from django.db.models import Count, Sum
from django import core

from .models import Bill
from .forms import BillForm, AmountPaidForm, SplitForm
def getNextSplitId():
	return Bill.objects.all().aggregate(Max('split_id'))['split_id__max'] + 1
@login_required
def index(request):
	current_user = request.user
	split_id_list = Bill.objects.all().values("split_id") \
		.annotate(split_id_count=Count("split_id")).order_by("-split_id")
	bill_list = []
	 
	for d in split_id_list:
		bill_list.append(Bill.objects.filter(split_id=d['split_id']))
	user_list = User.objects.filter(is_active=True)
	ledger = {}
	for u in user_list:
		if (u.id != current_user.id):
			ledger[u.first_name] = 0
	for sp in bill_list:
		for b in sp:
			b.owner_name = User.objects.filter(id=b.owner)[0].first_name
			b.debtor_name = User.objects.filter(id=b.debtor_id)[0].first_name
			if (not b.paid):
				if (current_user.id == b.owner):
					ledger[b.debtor_name] += b.amount
				elif (current_user.id == b.debtor_id):
					ledger[b.owner_name] -= b.amount
	bill_form = BillForm(current_user, initial={"owner": current_user.id}, 
						 auto_id="add-bill-%s", 
						 label_suffix="")
	context = {
				'user_list' : User.objects.filter(is_active=True),
				'current_user' : current_user,
				'bill_list' : bill_list,
				'ledger'    : ledger.items(),
				'bill_form' : bill_form
	}
	return render(request, 'BillSplitter/index.html', context)

def add_bill(request):
	form = BillForm(request.POST, 0)
	if form.is_valid():
		bill = form.save(commit=False)
		bill.split_id = getNextSplitId()
		bill.total = bill.amount
		if (bill.debtor_id == 0):
			user_list = User.objects.filter(is_active=True).exclude(id=bill.owner)
			split_amount = bill.amount / (len(user_list) + 1)
			for u in user_list:
				bill.pk = None #Make a new copy of the object
				bill.amount = split_amount
				bill.debtor_id = u.id
				bill.save()
			return redirect("bill-index")
		else:
			bill.save()
			return redirect("bill-index")
	else:
		return JsonResponse(request.POST)
		return redirect("bill-index")
		
def split_bill(request):
	form = SplitForm(request.POST)
	if form.is_valid():
		payees = request.POST.getlist("payee[]")
		bill = form.save(commit=False)
		bill.split_id = getNextSplitId()
		bill.total = bill.amount
		split_amount = bill.amount / len(payees)
		for i in payees:
			if (int(i) != bill.owner):
				bill.pk = None #Make a new copy of the object
				bill.amount = split_amount
				bill.debtor_id = int(i)
				bill.save()
			
		return redirect("bill-index")
	else:
		return redirect("bill-index")
		
def mark_amount_paid(request):
	if request.method == 'POST':
		form = AmountPaidForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			amount_remaining = cd.get("amount")
			
			bills = Bill.objects.filter(owner=cd.get("id")).filter(debtor_id=request.user.id).filter(paid=False).order_by("amount")
			for b in bills:
				
				if b.amount <= amount_remaining:
					amount_remaining = amount_remaining - b.amount
					b.paid = True
					b.save()
				else:
					b.amount = b.amount - amount_remaining
					b.save()
					amount_remaining = 0
					break
					
			if (amount_remaining > 0):
				new_bill = Bill.objects.create(
					 owner=request.user.id,
					 debtor_id=cd.get("id"),
					 amount=amount_remaining,
					 description="Overpayment",
					 paid=False)
				#new_bill.owner = request.user.id
				#new_bill.debtor_id = cd.get("id")
				#new_bill.amount = amount_remaining
				#new_bill.description = "Overpayment"
				new_bill.save()
			return redirect("bill-index")
		else:
			return JsonResponse(form.errors)

def delete_bill(request):
	if (request.GET['id']):
		bill = Bill.objects.get(id=request.GET['id'])
		if (bill.owner == request.user.id):
			bill.delete()
		
	return redirect("bill-index")

def mark_bill_paid(request):
	if (request.GET['id']):
		paid_bill = Bill.objects.get(id=request.GET['id'])
		paid_bill.paid = True
		paid_bill.paid_date = timezone.now()
		paid_bill.save()
		
	return redirect("bill-index")

def mark_bill_unpaid(request):
	if (request.GET['id']):
		paid_bill = Bill.objects.get(id=request.GET['id'])
		paid_bill.paid = False
		paid_bill.paid_date = timezone.now()
		paid_bill.save()
		
	return redirect("bill-index")