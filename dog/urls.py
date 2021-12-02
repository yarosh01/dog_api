from rest_framework.routers import DefaultRouter
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import DogViewSet, BreedViewSet


router = DefaultRouter()
router.register('dogs', DogViewSet, basename='dogs')
router.register('breeds', BreedViewSet, basename='breeds')

urlpatterns = [
    path('captcha/', include('rest_captcha.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += router.urls
