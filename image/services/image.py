from django.core.files.images import ImageFile
from django.db.models.query import Q

from image.models.image import Image


class ImageService:
    def get_default_image_name(self, image_file: ImageFile) -> str:
        default_name = "".join(image_file.name.split(".")[:-1])
        image_with_exact_name = Image.objects.filter(name=default_name)

        if image_with_exact_name.exists():
            images_with_similar_name = Image.objects.filter(name__iregex=rf"^{default_name} \(\d\)$")
            if images_with_similar_name.exists():
                similar_name_numbers = [
                    int(name.split("(")[-1].split(")")[0])
                    for name in images_with_similar_name.values_list("name", flat=True)
                ]
                similar_name_numbers.sort()

                default_name = f"{default_name} ({similar_name_numbers[-1] + 1})"
            else:
                default_name = f"{default_name} ({1})"

        return default_name
