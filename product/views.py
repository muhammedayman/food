from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, generics, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from customer.authentication import JWTCustomerAuthentication
from .models import *
from .serializer import *
# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
	queryset = Product.objects.all()
	filter_backends = [DjangoFilterBackend, filters.SearchFilter]
	filterset_fields = ['price','product_type__title','product_type__food_type__title']
	search_fields = ['^product_type__title',]
	authentication_classes=[JWTCustomerAuthentication,JWTAuthentication]
	permission_classes=[]
	
	def get_serializer_class(self):
		if self.action == 'create' or self.action == 'update':
			return ProductSaveSerializer
		return ProductDetailSerializer
class CategoryViewSet(viewsets.ModelViewSet):
	queryset = Category.objects.all()
	filter_backends = [DjangoFilterBackend, filters.SearchFilter]
	filterset_fields = ['food_type__title',]
	search_fields = ['^food_type__title',]
	authentication_classes=[JWTCustomerAuthentication,JWTAuthentication]
	permission_classes=[]
	
	def get_serializer_class(self):
		if self.action == 'create' or self.action == 'update':
			return CategorySaveSerializer
		return CategoryDetailSerializer