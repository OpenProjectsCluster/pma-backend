from rest_framework import serializers

from image.models.directory import Directory
from image.serializers.image import ImageSerializer
from user.serializers.custom_user import CustomUserSerializer


class DirectorySerializer(serializers.ModelSerializer):
    author = CustomUserSerializer(read_only=True)

    class Meta:
        model = Directory
        fields = ["id", "name", "author"]


class DirectoryDetailSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer(read_only=True)
    images = ImageSerializer(read_only=True, many=True)

    class Meta:
        model = Directory
        fields = ["id", "name", "author", "images"]
