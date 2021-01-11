from rest_framework import routers
from django.urls import path
from .views import StaffViewSet, Login,StaffSignup

router = routers.SimpleRouter()
router.register(r'staff', StaffViewSet, basename='staff')
router.register(r'staffsignup', StaffSignup, basename='staffsignup')
urlpatterns = [
	path('staff/login/', Login.as_view(), name='login' ),
]
urlpatterns += router.urls