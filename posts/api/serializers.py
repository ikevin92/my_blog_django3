from django.db.models.base import Model
# from rest_framework import fields
from rest_framework.serializers import ModelSerializer
from posts.models import Post


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title',
                  'description',
                  'order',
                  'created_At', ]
