from rest_framework import mixins, permissions, viewsets
from rest_framework.response import Response

from api_dir.blog.serializers import AuthorSerializer, PostSerializer
from core_dir.blog.models import Author, Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class AuthorViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
	viewsets.GenericViewSet
):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    #permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        #user = self.request.user
        queryset = Author.objects.all()
        #insert specific queryset logic here
        return queryset

    def get_object(self):
        #insert specific get_object logic here
        return super().get_object()

    def create(self, request, *args, **kwargs):
        serializer = AuthorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = AuthorSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = AuthorSerializer(instance=instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = AuthorSerializer(instance=instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request=request, *args, **kwargs)

