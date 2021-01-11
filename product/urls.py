from rest_framework import routers
from django.urls import path
from .views import ProductViewSet

router = routers.SimpleRouter()
router.register(r'products', ProductViewSet, basename='products')
urlpatterns = router.urls