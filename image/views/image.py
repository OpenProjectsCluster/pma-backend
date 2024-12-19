from django.db.models.query import QuerySet
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.serializers import BaseSerializer
from rest_framework.viewsets import ModelViewSet

from image.models.image import Image
from image.permissions.image import IsImageyAuthor
from image.serializers.image import ImageCreateSerializer, ImageSerializer
from image.services.image import ImageService


class ImageViewSet(ModelViewSet):
    queryset = Image.objects.all()

    def filter_queryset(self, queryset: QuerySet[Image]) -> QuerySet[Image]:
        if self.action == "list":
            queryset = queryset.filter(author=self.request.user)

        return queryset

    def get_permissions(self) -> list[BasePermission]:
        permissions = [IsAuthenticated()]

        if self.detail:
            permissions.append(IsImageyAuthor())

        return permissions

    def get_serializer_class(self) -> BaseSerializer:
        if self.action == "create":
            return ImageCreateSerializer

        return ImageSerializer

    def perform_create(self, serializer: ImageCreateSerializer) -> None:
        service = ImageService()
        default_name = service.get_default_image_name(serializer.validated_data["image"])
        serializer.save(author=self.request.user, name=default_name)
