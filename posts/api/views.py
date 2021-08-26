# rest_framework
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework import status
# models
from posts.models import Post
# serializer
from posts.api.serializers import PostSerializer


class PostModelViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    # http_method_names = ['get','put']
    

# class PostViewSet(ViewSet):
#     def list(self, request):
#         posts = PostSerializer(Post.objects.all(), many=True)
#         return Response(status=status.HTTP_200_OK, data=posts.data)

#     def retrieve(self, request, pk: int):
#         post = PostSerializer(Post.objects.get(pk=pk))
#         return Response(status=status.HTTP_200_OK, data=post.data)

#     def create(self, request):
#         serializer = PostSerializer(data=request.POST)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(status=status.HTTP_200_OK, data=serializer.data)


# class PostApiView(APIView):
#     def get(self, request):
#         posts = PostSerializer(Post.objects.all(), many=True)
#         return Response(status=status.HTTP_200_OK, data=posts.data)

#     def post(self, request):
#         serializer = PostSerializer(data=request.POST)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         print(serializer)
#         return Response(status=status.HTTP_200_OK, data=serializer.data)
