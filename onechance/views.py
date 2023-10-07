from rest_framework import viewsets
from rest_framework.response import Response

from .models import Post
from .serializeres import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
