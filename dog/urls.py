from rest_framework.routers import DefaultRouter
from .views import DogViewSet, BreedViewSet


router = DefaultRouter()
router.register('dogs', DogViewSet, basename='dogs')
router.register('breeds', BreedViewSet, basename='breeds')

urlpatterns = []

urlpatterns += router.urls
