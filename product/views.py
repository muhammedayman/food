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
	filterset_fields = ['price']
	search_fields = ['^product_code',]
    serializer_class=ProductDetailSerializer