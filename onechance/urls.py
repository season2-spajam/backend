from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, SingleImageViewSet

router = DefaultRouter()
router.register(r"posts", PostViewSet)
router.register(r"single_images", SingleImageViewSet)

urlpatterns = [] + router.urls
