from rest_framework import serializers
from .models import Orders

class CustomerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Orders
		exclude = ('created_at', 'updated_at')	

