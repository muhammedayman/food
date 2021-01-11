from rest_framework import serializers
from .models import Product,Category
from drf_writable_nested.serializers import WritableNestedModelSerializer

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		exclude = ('created_at', 'updated_at','product_type')	
class CategoryDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		exclude = ('created_at', 'updated_at')	

class ProductSaveSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
	product_type=CategorySerializer(required=True)
	class Meta:
		model = Product
		exclude = ('created_at', 'updated_at')	
	def to_internal_value(self, data):
		data['vendor_staff']=self.context['request'].user.staff
		return data		
class ProductDetailSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
	product_type=CategoryDetailSerializer(required=True)
	class Meta:
		model = Product
		exclude = ('created_at', 'updated_at')	
	def to_internal_value(self, data):
		data['vendor_staff']=self.context['request'].user.staff
		return data		

		