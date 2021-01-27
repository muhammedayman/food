from django.db import models
from staffs.models import Staff
from shared.models import BaseModel
from customer.models import Customer
from product.models import Product
# Create your models here.

class Orders(BaseModel):
	user_customer=models.OneToOneField(Customer, on_delete=models.CASCADE,related_name="user_customer")
	products=models.ForeignKey(Product, related_name='products', on_delete=models.CASCADE)
	quantity=models.PositiveIntegerField()
	price=models.FloatField(default=0)
	net_amout=models.FloatField(default=0)
	gross_amount=models.FloatField(default=0)
	tax=models.FloatField(default=0)
	offer=models.FloatField(default=0)
	date_order=models.DateTimeField(null=True, blank=True)
	date_dispatch=models.DateTimeField(null=True, blank=True)
	is_returned=models.BooleanField(default=False)
	is_delivered=models.BooleanField(default=False)
	is_cancelled=models.BooleanField(default=False)
	comments=models.CharField(max_length=200, blank=True, null=True)
	statuses = [
		('DRAFT', 'Draft'),
		('ACTIVE', 'Active'),
		('INACTIVE', 'InActive'),
		('BOOKINGCMPLTD', 'Booking Completed'),
		('COMPLETED', 'Completed')
	]
	status = models.CharField(max_length= 100, choices=statuses, default="DRAFT")
	
	class Meta:
		db_table = 'orders'
