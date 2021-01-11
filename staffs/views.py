from django.shortcuts import render
from .models import *
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, generics, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from django.conf import settings
from .permissions import IsStaff
from shared.serializer import OtpSerializer
from .serializer import *
from shared.models import Otp

class Login(TokenObtainPairView):
	serializer_class = LoginSerializer

class StaffSignup(viewsets.ModelViewSet):
	permission_classes = []
	queryset = Staff.objects.all()

	def get_serializer_class(self):
		if self.action == 'create':
			import pdb ; pdb.set_trace()
			return StaffCreateSerializer
		return StaffSerializer

	@action(detail=False, methods=['post'])
	def signup(self, request):
		serializer = CustomerSignUpSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			serializer_otp = OtpSerializer(data=request.data)
			if serializer_otp.is_valid():
				serializer_otp.save()
			return Response({'otp': serializer_otp.data,'customer': serializer.data})
		else:
			return Response({'status': 'failure', 'errors': serializer.errors}, status=400)

class StaffViewSet(viewsets.ModelViewSet):
	permission_classes = []
	queryset = Staff.objects.all()
	filter_backends = [DjangoFilterBackend,filters.SearchFilter]
	filterset_fields = ['role']
	search_fields = ['^name']

	def get_serializer_class(self):
		if self.action == 'create':
			return StaffCreateSerializer
		return StaffSerializer

	@action( detail=False,methods=['GET'] ,permission_classes = [])
	def profile(self,request):
		queryset=Staff.objects.get(id=request.user.staff.id)
		serializer=ProfileSerailizer(queryset)
		return Response(serializer.data,status=200)

	@action( detail=False,methods=['POST'] ,permission_classes = [])
	def forgot_password(self, request):
		phone_number = request.data.get('phone_number')
		staff = Staff.objects.filter(phone_number=phone_number).first()
		if not staff:
			return Response({'status': 'failure', 'errors': "User does not exist, please signup"})
		existing_otp = Otp.find_existing_otp(phone_number, "RESET_PASSWORD")
		if existing_otp:
			serializer = OtpSerializer(existing_otp, data={}, partial=True)
		else:
			serializer = OtpSerializer(data={'phone_number': phone_number, 'verification_type': 'RESET_PASSWORD'})
		if serializer.is_valid():
			serializer.save()
			return Response({'status': 'success', 'phone_number': phone_number, 'validity_in_minutes': 2, 'message': f"OTP sent to {phone_number}"}, status=200)
		else:
			return Response({'status': 'failure', 'errors': serializer.errors}, status=400)

	@action( detail=False, methods=['POST'], permission_classes = [])
	def change_password(self, request):
		serializer = StaffOtpChangePasswordSerializer(data=request.data)
		phone_number = request.data.get('phone_number')
		if not serializer.is_valid():
			return Response({'status': 'failure', 'errors': serializer.errors}, status=400)
		otp = Otp.find_existing_otp(phone_number, 'RESET_PASSWORD')
		if not otp:
			return Response({'status': 'failure', 'errors': ["OTP expired!"]}, status=400)
		if otp.otp != serializer.data.get('otp'):
			return Response({'status': 'failure', 'errors': ["Invalid OTP"]}, status=400)
		staff = Staff.objects.filter(phone_number=phone_number).first()	
		staff.set_password(serializer.data.get('password'))
		staff.save()
		return Response({'status': 'success', 'message': 'Password updated'})

class ProfileSerailizer(serializers.ModelSerializer):
	user_name=serializers.SerializerMethodField()
	
	class Meta:
		model=Staff
		fields=['name','user_name','phone_number','email','role','user_category']
	
	def get_user_name(self,instance):
		return instance.auth_user.username