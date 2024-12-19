from django.urls import include, path
from rest_framework.routers import DefaultRouter

from image.views.directory import DirectoryViewSet
from image.views.image import ImageViewSet

router = DefaultRouter()
router.register("directory", DirectoryViewSet)
router.register("image", ImageViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
