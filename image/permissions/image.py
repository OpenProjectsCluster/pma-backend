from typing import Any

from rest_framework.permissions import BasePermission
from rest_framework.request import HttpRequest

from image.models.image import Image


class IsImageyAuthor(BasePermission):
    def has_permission(self, request: HttpRequest, view: Any) -> bool:
        return super().has_permission(request, view)

    def has_object_permission(self, request: HttpRequest, _: Any, obj: Image) -> bool:
        return obj.author == request.user
