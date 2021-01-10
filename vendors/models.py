from django.db import models
from shared.models import BaseModel
from staffs.models import Staff


class Vendor(BaseModel):
	name = models.CharField(max_length=50)
	code = models.CharField(max_length=12, unique=True)
	website = models.CharField(max_length=100)
	description = models.TextField()

	class Meta:
		db_table = 'vendors'

	def __str__(self):
		return self.name