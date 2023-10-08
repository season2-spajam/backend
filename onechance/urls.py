from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, SingleImageViewSet, PostWithImageUrlViewSet

router = DefaultRouter()
router.register(r"posts", PostViewSet)
router.register(r"posts_with_image_url", PostWithImageUrlViewSet)
router.register(r"single_image", PostWithImageUrlViewSet)

urlpatterns = [] + router.urls
