from typing import Any

from django.contrib import admin
from django.utils.html import format_html

from image.models.directory import Directory
from image.models.image import Image


class ImageAdmin(admin.ModelAdmin):
    model = Image
    list_display = [
        "author",
        "image_tag",
    ]

    def image_tag(self, obj: Image) -> Any:
        return format_html(
            f'<img src="{obj.image.url if obj.image else ''}" style="max-width:200px; max-height:200px"/>'
        )


admin.site.register(Directory)
admin.site.register(Image, ImageAdmin)
