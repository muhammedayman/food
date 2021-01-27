from django.shortcuts import render
from rest_framework import viewsets 
from .models import *
from orders.models import *
from .serializer import *
from shared.models import *
from shared.serializer import *
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class Customer_view(viewsets.ModelViewSet):
	authentication_classes=[]
	permission_classes=[]
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer

	@action(detail=False, methods=['post'])
	def generate_otp(self, request):
		serializer = OtpSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=200)
		else:
			return Response({'status': 'failure', 'errors': serializer.errors}, status=400)	

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

	@action(detail=False, methods=['post'])
	def verify_otp(self, request):
		serializer = VerifyOtpSerializer(data=request.data)
		if serializer.is_valid():
			recent_otp = Otp.objects.filter(phone_number=serializer.data['phone_number'], is_verified=False).last()
			if not recent_otp:
				return Response({'status': 'failure', 'errors': ['No otp found']}, status=400)
			if not recent_otp.otp == serializer.data.get('otp'):
				return Response({'status': 'failure', 'errors': ['Invalid Otp']}, status=400)
			data = dict(last_login_at= datetime.now(), **serializer.data)
			del data['otp']
			customer= Customer.objects.filter(phone_number=data['phone_number']).first()
			if not customer:
				return Response({'status': 'failure', 'errors': ['user not found']}, status=400)
			customer.last_login_at=datetime.now()
			customer.save()
			recent_otp.is_verified = True
			recent_otp.save()
			order=Orders.objects.filter(user_customer=customer).last()
			order_id=self.request.GET.get("order_id")
			if not order_id and order:
				order_id=order.id
			if order_id:
				order_object=Orders.objects.get(id=order_id)
				customer.draft_order=order_object
				customer.save(update_fields=['draft_order'])
			return Response({'token': customer.generate_token(), **CustomerSerializer(customer).data})
		else:
			return Response({'status': 'failure', 'errors': serializer.errors}, status=400)
