# Generated by Django 3.0.4 on 2021-01-10 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('staffs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.CharField(blank=True, max_length=100, null=True)),
                ('context_text', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'categorys',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product_code', models.CharField(blank=True, max_length=50, null=True)),
                ('quantity', models.PositiveIntegerField()),
                ('ratings', models.PositiveIntegerField()),
                ('price', models.FloatField(default=0)),
                ('net_amout', models.FloatField(default=0)),
                ('gross_amount', models.FloatField(default=0)),
                ('tax', models.FloatField(default=0)),
                ('offer', models.FloatField(default=0)),
                ('date_order', models.DateTimeField(blank=True, null=True)),
                ('date_dispatch', models.DateTimeField(blank=True, null=True)),
                ('is_returned', models.BooleanField(default=False)),
                ('vendor_staff', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='vendor_staff', to='staffs.Staff')),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='product_category', to='product.Category')),
                ('product_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='product.Product')),
            ],
            options={
                'db_table': 'product_categorys',
            },
        ),
    ]
