from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('rest_registration.api.urls')),
    path('api-login/', obtain_auth_token, name='api_login'),
    path('blog/', include('blog.urls')),
    path('', include('core.urls')),
]
