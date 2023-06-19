from rest_framework import serializers
from . import models


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Post
        fields = ["header", "body", "slug"]


class PostGroupSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True)

    class Meta:
        model = models.PostGroup
        fields = '__all__'
