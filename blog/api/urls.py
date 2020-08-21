from django.urls import path, include
from rest_framework import routers
from .views import BlogView


router = routers.DefaultRouter()
router.register('', BlogView)

urlpatterns = [
    path('', include(router.urls)),
]
