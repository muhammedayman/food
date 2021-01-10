from django.db import models
from staff.models import Staff
from shared.models import BaseModel
from customers.models import Customer

# Create your models here.
class Orders(BaseModel):
    user_customer=models.OneToOneField(Customer, on_delete=models.CASCADE,related_name="user_customer")
    product_id=models.PositiveIntegerField()
    quantity=models.PositiveIntegerField()
    price=models.FloatField(default=0)
    net_amout=models.FloatField(default=0)
    gross_amount=models.FloatField(default=0)
    tax=models.FloatField(default=0)
    offer=models.FloatField(default=0)
    date_order=models.DateTimeField(null=True, blank=True)
    date_dispatch=models.DateTimeField(null=True, blank=True)
    is_returned=models.BooleanField(default=False)
    
    class Meta:
        db_table = 'orders'
