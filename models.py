from django.db import models
from django.utils import timezone

# Create your models here.
		
class Bill(models.Model):
	owner = models.IntegerField()
	debtor_id = models.IntegerField()
	created_date = models.DateTimeField(default=timezone.now)
	paid = models.BooleanField(default=False)
	paid_date = models.DateTimeField(blank=True, null=True)
	split_id = models.IntegerField()
	description = models.TextField()
	amount = models.DecimalField(default=0, decimal_places=2, max_digits=7)
	total = models.DecimalField(default=0, decimal_places=2, max_digits=7)
	
	class Meta:
		ordering = ['-created_date',]
	
	def __str__(self):
		return self.description