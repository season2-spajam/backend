from rest_framework import serializers

from .models import Post, SingleImage


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id", 
            "handle_name", 
            "img", 
            "good_count",
            "caption", 
            "created_at"
        )

class SingleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SingleImage
        fields = ("img",)