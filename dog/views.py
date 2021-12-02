import django_filters
from rest_framework import viewsets, status
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_framework_simplejwt.views import TokenRefreshView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Dog, Breed
from .serializers import DogSerializer, BreedSerializer, DogPhotoSerializer


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


class GoogleLogin(SocialLoginView):
    authentication_classes = []
    adapter_class = GoogleOAuth2Adapter
    callback_url = "http://localhost:3000"
    client_class = OAuth2Client

@csrf_exempt
def google_token(request):
    if "code" not in request.body.decode():
        class RefreshNuxtAuth(TokenRefreshView):

            def post(self, request, *args, **kwargs):
                request.data._mutable = True
                request.data["refresh"] = request.data.get("refresh_token")
                request.data._mutable = False
                response = super().post(request, *args, **kwargs)
                response.data['refresh_token'] = response.data['refresh']
                response.data['access_token'] = response.data['access']
                return response

        return RefreshNuxtAuth.as_view()(request)
    return GoogleLogin.as_view()(request)


class DogPhotoUpload(APIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = ()

    def post(self, request):
        serializer = DogPhotoSerializer(data=request.data, instance=request.user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
