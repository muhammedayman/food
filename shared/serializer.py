from rest_framework import serializers
from .models import Otp

class OtpSerializer(serializers.ModelSerializer):
	phone_number = serializers.RegexField("[0-9]", max_length=12, min_length=10, allow_blank=False)

	class Meta:
		model = Otp
		fields = '__all__'

class VerifyOtpSerializer(serializers.Serializer):
	phone_number = serializers.RegexField("[0-9]", max_length=12, min_length=10, allow_blank=False)
	email = serializers.CharField(required=False,allow_blank=True,max_length=150)
	otp = serializers.CharField(required=True)		