from django.db import models

# Create your models here.
class Product(BaseModel):
    vendor_staff=models.OneToOneField(Staff, on_delete=models.CASCADE,related_name="vendor_staff")
    product_id=models.PositiveIntegerField()
    quantity=models.PositiveIntegerField()
    ratings=models.PositiveIntegerField()
    price=models.FloatField(default=0)
    net_amout=models.FloatField(default=0)
    gross_amount=models.FloatField(default=0)
    tax=models.FloatField(default=0)
    offer=models.FloatField(default=0)
    date_order=models.DateTimeField(null=True, blank=True)
    date_dispatch=models.DateTimeField(null=True, blank=True)
    is_returned=models.BooleanField(default=False)
    
    class Meta:
        db_table = 'products'

class Category(BaseModel):
    title=models.CharField(max_length=100,null=True, blank=True)
    slug=models.CharField(max_length=100,null=True, blank=True)
    context_text=models.CharField(max_length=100,null=True, blank=True)

    class Meta:
        db_table = 'categorys'

class ProductCategory(BaseModel):
    product_id=models.OneToOneField(Product, on_delete=models.CASCADE,related_name="product")
    category_id=models.OneToOneField(Category, on_delete=models.CASCADE,related_name="product_category")

    class Meta:
        db_table = 'product_categorys'