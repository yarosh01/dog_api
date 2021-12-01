import django_filters
from rest_framework import viewsets
from .models import Dog, Breed
from .serializers import DogSerializer, BreedSerializer


class BorrowedFilterSet(django_filters.FilterSet):
    missing = django_filters.BooleanFilter(field_name="returned", lookup_expr="isnull")
    overdue = django_filters.BooleanFilter(method="get_overdue", field_name="returned")

    class Meta:
        model = Breed
        fields = ["size"]

    def get_overdue(self, queryset, value):
        if value:
            return queryset.overdue()
        return queryset


class DogViewSet(viewsets.ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer


class BreedViewSet(viewsets.ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    filterset_class = BorrowedFilterSet
