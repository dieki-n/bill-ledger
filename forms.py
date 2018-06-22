from django import forms
from .models import Bill
from django.contrib.auth.models import User

def generateUserList(user_list):
	l = []
	for u in user_list:
		l.append((u.id, u.first_name))
	return l
		
class AmountPaidForm(forms.Form):
	id = forms.IntegerField(required=True)
	amount = forms.DecimalField(required=True, decimal_places=2)

class BillForm(forms.ModelForm):
	#debtor_id = forms.ChoiceField(choices=[(0, "Everyone")] + generateUserList(User.objects.all()), label="")
	#owner = forms.ChoiceField(choices=generateUserList(User.objects.all()), label="owes")
	#description = forms.CharField(label="for", max_length=100)
	#amount = forms.CharField(label="the amount of $")
	#def __init__(self, user, *args, **kwargs):
	#	super(BillForm, self).__init__(*args, **kwargs)
	#	self.fields['debtor_id'] = forms.ChoiceField(choices=[(0, "Everyone")] + generateUserList(User.objects.all()), label="")
	#	self.fields['owner'] = forms.ChoiceField(choices=generateUserList(User.objects.all()), label="owes")
	class Meta:
		model = Bill
		fields = ('debtor_id', 'owner', 'amount', 'description')

class SplitForm(forms.ModelForm):
	class Meta:
		model = Bill
		fields = ('owner', 'amount', 'description')
	
		