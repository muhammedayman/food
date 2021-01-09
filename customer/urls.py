from rest_framework import routers
from django.urls import path
from .views import Customer_view

router = routers.SimpleRouter()
router.register(r'customers', Customer_view, basename='customers')
urlpatterns = router.urls