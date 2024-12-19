from __future__ import annotations

from pathlib import Path

from django.contrib.auth import get_user_model
from django.db import models

from image.models.directory import Directory


def get_image_upload_path(instance: Image, filename: str) -> str:
    return Path("image", f"user_{instance.author.pk}", filename)


class Image(models.Model):
    image = models.ImageField(upload_to=get_image_upload_path)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="images")
    directory = models.ForeignKey(Directory, on_delete=models.CASCADE, related_name="images")
    name = models.CharField(max_length=255)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["name", "directory"], name="unique image name per directory")]

    def __str__(self) -> str:
        return self.name
