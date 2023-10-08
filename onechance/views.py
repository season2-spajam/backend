from io import BytesIO

import requests
import string, random

# 日時を扱う django のモジュールをインポート
from django.utils import timezone
from PIL import Image
from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Post, SingleImage
from .serializeres import (
    PostSerializer,
    PostWithImageUrlSerializer,
    SingleImageSerializer,
)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = Post.objects.all()
        # クエリパラメータに "filter=today" があれば、created_at が今日のものだけを返す
        param_filter = self.request.query_params.get("filter", None)
        if param_filter == "today":
            queryset = queryset.filter(
                created_at__gte=timezone.now().replace(
                    hour=0, minute=0, second=0, microsecond=0
                )
            )
        return queryset


class SingleImageViewSet(viewsets.ModelViewSet):
    queryset = SingleImage.objects.all()
    serializer_class = SingleImageSerializer

class PostWithImageUrlViewSet(viewsets.ViewSet):
    serializer_class = PostWithImageUrlSerializer
    queryset = Post.objects.all()

    def list(self, request):
        return Response(
            PostSerializer(self.queryset, many=True).data,
            status=status.HTTP_200_OK,
        )

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            # シリアライザーのcreateメソッドを呼び出してPostオブジェクトを作成
            print(serializer.validated_data)
            post = serializer.save()
            # post を json にして返す
            return Response(PostSerializer(post).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
