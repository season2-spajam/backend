from django.core.files.base import ContentFile
from rest_framework import serializers
from urllib.parse import urlparse

from .models import Post, SingleImage
from PIL import Image
from io import BytesIO
import requests

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

import random, string
def randomCharacter(n):
    c = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return ''.join([random.choice(c) for i in range(n)])

class PostWithImageUrlSerializer(serializers.Serializer):
    handle_name = serializers.CharField(max_length=255)
    caption = serializers.CharField(allow_blank=True, required=False)
    img_url = serializers.CharField()  # img_urlフィールドを手動で定義

    def create(self, validated_data):
        url = validated_data.pop("img_url")
        parsed_url = urlparse(url)
        # 拡張子を除いたファイル名を取得
        filename = parsed_url.path.split("/")[-1].split(".")[0]

        response = requests.get(url)
        filename += randomCharacter(10)
        with open(f"media/images/{filename}.png", "wb") as f:
            f.write(response.content)
        response.raise_for_status()

        image = Image.open(f"media/images/{filename}.png")

        print("image", image)

        caption = validated_data.pop("caption")
        handle_name = validated_data.pop("handle_name")

        post = Post.objects.create(
            img=f"images/{filename}.png",
            caption=caption,
            handle_name=handle_name,
        )
        return post
