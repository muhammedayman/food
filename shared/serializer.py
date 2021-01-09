from rest_framework import serializers
from .models import Otp

class OtpSerializer(serializers.ModelSerializer):
	phone_number = serializers.RegexField("[0-9]", max_length=12, min_length=10, allow_blank=False)

	class Meta:
		model = Otp
		fields = '__all__'