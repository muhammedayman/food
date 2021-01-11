from rest_framework import serializers
from .models import Staff
from drf_writable_nested.serializers import WritableNestedModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class StaffCreateSerializer(serializers.ModelSerializer):
	username = serializers.CharField(write_only= True)
	password = serializers.CharField(write_only= True)

	class Meta:
		model = Staff
		fields = ('name', 'email', 'phone_number','username', 'password', 'employee_code', "role", "user_category")


class StaffOtpChangePasswordSerializer(serializers.Serializer):
	phone_number = serializers.RegexField("[0-9]", max_length=12, min_length=10, allow_blank=False)
	otp = serializers.CharField(required=True, max_length=6, min_length=6)
	password = serializers.CharField(required=True, max_length=50, min_length=6)
	confirmation_password = serializers.CharField(required=True, max_length=50, min_length=6)

	def validate(self, data):
		if data.get('password') != data.get('confirmation_password'):
			raise serializers.ValidationError("Password should match with confirmation password")
		return data

class LoginSerializer(TokenObtainPairSerializer):
	@classmethod
	def get_token(cls, user):
		token = super().get_token(user)
		return token

	def validate(self, attrs):
		data = super(LoginSerializer, self).validate(attrs)
		if not self.user:
			raise serializers.ValidationError("details", "Please check username and password")

		staff = self.user.staff
		if staff:
			if staff.is_active:
				data.update({'staff': StaffSerializer(self.user.staff).data})
				return data
			else:
				if not staff.active:
					raise serializers.ValidationError("details", "Your account is deactivated")
				
		else:
			return serializers.ValidationError("details", "Please Contact Admin")
class StaffSerializer(serializers.ModelSerializer):
	class Meta:
		model = Staff
		fields = ('id', 'name', 'email', 'phone_number','employee_code',  "role", 'user_category')
