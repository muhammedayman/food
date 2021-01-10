from django.db import models

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from shared.models import BaseModel

class StaffManager(models.Manager):
    def create(self, email=None,username=None, password=None, **kwargs):
        user = User(username=username,password=make_password(password),is_staff=True)
        user.save()
        
        staff = Staff(auth_user=user, email=email, **kwargs)
        staff.save()
        return staff
    
class Staff(BaseModel):
	ROLES = [
		('ADMIN', 'Admin'),
		('MANAGER', 'Manager'),
		('SUPERVISOR', "Supervisor"),
		('EMPLOYEE', 'Employee')
	]
	auth_user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	phone_number = models.CharField(max_length= 15, null=True, blank=True)
	email = models.CharField(max_length=50)
	employee_id = models.CharField(max_length=50, null=True, blank=True)
	active = models.BooleanField(default = True)
	employer_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
	employer_id = models.PositiveIntegerField()
	employer = GenericForeignKey('employer_content_type', 'employer_id')
	role = models.CharField(null=True, blank=True, choices=ROLES, max_length=20)
	picture=models.ImageField(upload_to='pictures/%d/%m/%Y',max_length=255, null=True, blank=True)


	class Meta:
		db_table = 'staff'

	def __str__(self):
		return self.name
	objects = StaffManager()

	def vendor(self):
		if self.employer_content_type.model == 'vendors':
			return self.employer
		else:
			return self.employer.vendor