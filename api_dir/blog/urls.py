from django.urls import include, path
from rest_framework import routers

from api_dir.blog.views import AuthorViewSet, PostViewSet

router = routers.DefaultRouter()

router.register(r'posts', PostViewSet)
router.register(r'authors', AuthorViewSet)

urlpatterns = [
    path("", include(router.urls)),
]