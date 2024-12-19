from django.contrib.auth import get_user_model
from django.db import models


class Directory(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["name", "author"], name="unique directory name per user")]

    def __str__(self) -> str:
        return self.name
