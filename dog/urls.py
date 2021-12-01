from rest_framework.routers import DefaultRouter
from .views import DogViewSet, BreedViewSet
from django.urls import path, include


router = DefaultRouter()
router.register('dogs', DogViewSet, basename='dogs')
router.register('breeds', BreedViewSet, basename='breeds')

urlpatterns = [
    path('captcha/', include('rest_captcha.urls'))
]

urlpatterns += router.urls
