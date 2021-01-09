from django.shortcuts import render
from rest_framework import viewsets 
from .models import *
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