from django.urls import path, include
from rest_framework import routers
from .views import home


urlpatterns = [
    path('api/', include('blog.api.urls')),
    path('', home),
]