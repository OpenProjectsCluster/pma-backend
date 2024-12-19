from typing import Any

from rest_framework.permissions import BasePermission
from rest_framework.request import HttpRequest

from image.models.directory import Directory


class IsDirectoryAuthor(BasePermission):
    def has_permission(self, request: HttpRequest, view: Any) -> bool:
        return super().has_permission(request, view)

    def has_object_permission(self, request: HttpRequest, _: Any, obj: Directory) -> bool:
        return obj.author == request.user
