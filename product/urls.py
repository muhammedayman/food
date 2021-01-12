from rest_framework import routers
from django.urls import path
from .views import ProductViewSet
from fooddelivery import settings
from django.conf.urls.static import static

router = routers.SimpleRouter()
router.register(r'products', ProductViewSet, basename='products')
urlpatterns = router.urls

if True:
	urlpatterns += static (
		settings.STATIC_URL,
		document_root=settings.STATIC_ROOT
	)
	urlpatterns+=static(
	settings.MEDIA_URL,
	document_root=settings.MEDIA_ROOT
	)