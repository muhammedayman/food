from django.db import models
from shared.models import BaseModel
import jwt, random, datetime, time
import uuid
from django.conf import settings
from django.db.models.signals import pre_save
from django.contrib.contenttypes.fields import GenericRelation

class Customer(BaseModel):
	first_name = models.CharField(max_length=150, null=True, blank=True)
	last_name = models.CharField(max_length=150, null=True, blank=True)
	email = models.CharField(max_length=50, null=True, blank=True)
	phone_number =  models.CharField(max_length=20, unique=True, db_index=True)
	last_login_at = models.DateTimeField(null=True)
	is_active = models.BooleanField(default=True)
	draft_order = models.ForeignKey('orders.Orders', on_delete=models.CASCADE, null=True)
	uid = models.UUIDField(default=uuid.uuid4,unique=True)

	def generate_token(self):
		dt = datetime.datetime.now() + datetime.timedelta(days=15)
		token = jwt.encode({
			'id': self.id,
			'exp': int(time.mktime(dt.timetuple()))
			}, settings.SECRET_KEY, algorithm='HS256')
		return token.decode('utf-8')

	class Meta:
		db_table = 'customers'

	@property
	def is_authenticated(self):
		return True

	def is_guest(self):
		return self.phone_number == '0'
	
	@property	
	def name(self):
		return f'{self.first_name} {self.last_name}'
	

def add_uid(sender,instance,**kwargs):
	if instance.id is None:
		instance.uid=uuid.uuid4()
		while Customer.objects.filter(uid=instance.uid).exists():
			instance.uid=uuid.uuid4()
	return instance.uid
	
pre_save.connect(add_uid,sender=Customer)