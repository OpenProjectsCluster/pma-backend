from rest_framework import serializers

from image.models.image import Image
from user.serializers.custom_user import CustomUserSerializer


class ImageSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer(read_only=True)

    class Meta:
        model = Image
        fields = ["id", "image", "author", "directory", "name"]


class ImageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ["id", "image", "directory"]
