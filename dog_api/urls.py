from django.contrib import admin
from django.urls import path, include
from dog.views import GoogleLogin, google_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('dog.urls')),
    path('api/v2/', include('dog.urls_v2')),
    path('auth/', include('dj_rest_auth.urls')),
    path('social-login/google/', GoogleLogin.as_view(), name='google_login'),
    path('social-login/google/', google_token, name='google_login'),
]
