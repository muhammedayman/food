from rest_framework import serializers
from .models import Customer
from shared.models import Otp
class CustomerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Customer
		fields = ('first_name', 'last_name', 'email', 'phone_number', 'last_login_at', 'is_active', 'uid')

class CustomerSignUpSerializer(serializers.ModelSerializer):
	class Meta:
		model = Customer
		fields = ('first_name','last_name', 'email', 'phone_number')

class OtpSerializer(serializers.ModelSerializer):
	phone_number = serializers.RegexField("[0-9]", max_length=12, min_length=10, allow_blank=False)

	class Meta:
		model = Otp
		fields = '__all__'		