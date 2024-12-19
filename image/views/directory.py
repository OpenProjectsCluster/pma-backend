from django.db.models.query import QuerySet
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.serializers import BaseSerializer
from rest_framework.viewsets import ModelViewSet

from image.models.directory import Directory
from image.permissions.directory import IsDirectoryAuthor
from image.serializers.directory import DirectoryDetailSerializer, DirectorySerializer


class DirectoryViewSet(ModelViewSet):
    queryset = Directory.objects.all()

    def filter_queryset(self, queryset: QuerySet[Directory]) -> QuerySet[Directory]:
        if self.action == "list":
            queryset = queryset.filter(author=self.request.user)

        return queryset

    def get_permissions(self) -> list[BasePermission]:
        permissions = [IsAuthenticated()]

        if self.detail:
            permissions.append(IsDirectoryAuthor())

        return permissions

    def get_serializer_class(self) -> BaseSerializer:
        if self.action == "retrieve":
            return DirectoryDetailSerializer

        return DirectorySerializer

    def perform_create(self, serializer: DirectorySerializer) -> None:
        serializer.save(author=self.request.user)
