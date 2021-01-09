from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Customer
		fields = ('first_name', 'last_name', 'email', 'phone_number', 'last_login_at', 'is_active', 'uid')

class CustomerSignUpSerializer(serializers.ModelSerializer):
	class Meta:
		model = Customer
		fields = ('first_name','last_name', 'email', 'phone_number')
		