from django.contrib import admin
from django.urls import path, include
from dog.views import GoogleLogin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('dog.urls')),
    path('auth/', include('dj_rest_auth.urls')),
    path('social-login/google/', GoogleLogin.as_view(), name='google_login'),
]
