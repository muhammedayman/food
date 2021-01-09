# Generated by Django 3.0.4 on 2021-01-08 15:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(blank=True, max_length=150, null=True)),
                ('last_name', models.CharField(blank=True, max_length=150, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_number', models.CharField(db_index=True, max_length=20, unique=True)),
                ('last_login_at', models.DateTimeField(null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('uid', models.UUIDField(default=uuid.uuid4, unique=True)),
            ],
            options={
                'db_table': 'customers',
            },
        ),
    ]
