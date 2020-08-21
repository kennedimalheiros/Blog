from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import Blog
from .serializers import BlogSerializer


class BlogView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
