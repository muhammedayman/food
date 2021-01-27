from django.db import models
from datetime import datetime
from model_utils import Choices
from django.utils.translation import gettext_lazy as _
from django.db.models import Q
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
import random, math
# Create your models here.
class BaseModel(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True

	@classmethod
	def to_date_time(self,timestamp):
		return datetime.fromtimestamp(timestamp)

	@classmethod
	def to_timestamp(self, time):
		return datetime.timestamp(time)

class Otp(BaseModel):
	TYPES = Choices(('REGISTRATION', 'Registration', _('registration')),
				('BOOKING', 'Booking', _('booking')),
				('LOGIN', 'Login', _('login')),
				('RESET_PASSWORD', 'Reset Password', _('reset_password')))
	phone_number = models.CharField(max_length=20, db_index=True)
	country_code = models.CharField(max_length=8)
	email = models.CharField(max_length=150,null=True, blank=True)
	otp = models.CharField(max_length=10, null=True, blank=True)
	otp_sent_at = models.DateTimeField(null=True)
	is_verified = models.BooleanField(default=False)
	verification_type = models.CharField(max_length=25, choices=TYPES, default='REGISTRATION')

	class Meta:
		db_table = 'otps'

	@classmethod
	def find_existing_otp(self, contact, verification_type=None):
		import datetime
		otps = self.objects.filter(phone_number=contact, is_verified=False)
		if verification_type:
			otps = otps.filter(verification_type=verification_type)
		return otps.filter(Q(otp_sent_at=None)|Q(otp_sent_at__gte = datetime.datetime.now()-datetime.timedelta(minutes=2))).first()

@receiver(pre_save, sender=Otp)
def generate_otp(sender, instance,  **kwargs):
	if instance.id:
		return 
	otp = str(random.random())[2:8]
	instance.otp=otp
	instance.otp_sent_at=datetime.now()