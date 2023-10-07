from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="handle_name")
    imgUrl = serializers.ImageField(source="img")
    goodCount = serializers.IntegerField(source="good_count")
    createdAt = serializers.DateTimeField(source="created_at")

    class Meta:
        model = Post
        fields = ("id", "user", "imgUrl", "goodCount", "createdAt")
