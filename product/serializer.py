from rest_framework import serializers
from .models import Product,Category,ProductCategory


class CategorySerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Category
		exclude = ('created_at', 'updated_at')	
class ProductCategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = ProductCategory
		exclude = ('created_at', 'updated_at')	
class ProductSaveSerializer(serializers.ModelSerializer):

	class Meta:
		model = Product
		exclude = ('created_at', 'updated_at','product_categorys')	
class ProductSaveSerializer(serializers.ModelSerializer):

	class Meta:
		model = Product
		exclude = ('created_at', 'updated_at','product_categorys')	

class ProductDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ('created_at', 'updated_at')	
		