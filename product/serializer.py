from rest_framework import serializers
from .models import Product,Category,FoodType
from drf_writable_nested.serializers import WritableNestedModelSerializer

class FoodTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = FoodType
		exclude = ('created_at', 'updated_at')	
class CategorySaveSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
	food_type=FoodTypeSerializer(required=True)
	class Meta:
		model = Category
		exclude = ('created_at', 'updated_at')	
class CategoryDetailSerializer(serializers.ModelSerializer):
	food_type=FoodTypeSerializer(required=True)
	class Meta:
		model = Category
		exclude = ('created_at', 'updated_at')	

class ProductSaveSerializer(serializers.ModelSerializer):
	product_type=serializers.PrimaryKeyRelatedField(read_only=True)
	class Meta:
		model = Product
		exclude = ('created_at', 'updated_at')	
	def to_internal_value(self, data):
		# import pdb ; pdb.set_trace()
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

		