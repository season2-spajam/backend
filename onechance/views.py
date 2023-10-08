from rest_framework import viewsets

from .models import Post, SingleImage
from .serializeres import PostSerializer, SingleImageSerializer

# 日時を扱う django のモジュールをインポート
from django.utils import timezone


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