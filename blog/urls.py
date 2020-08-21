from django.urls import path, include
from .views import home


urlpatterns = [
    path('api/', include('blog.api.urls')),
    path('', home),
]