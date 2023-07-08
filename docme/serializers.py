from rest_framework import serializers
from . import models


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Post
        fields = ["header", "body", "slug"]
        extra_kwargs = {
            "slug": {"read_only": True}
        }


class PostGroupSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, required=False)

    class Meta:
        model = models.PostGroup
        fields = '__all__'

    def create(self, validated_data: dict):
        postgroup = models.PostGroup.objects.create(
            title=validated_data.get("title"))
        if validated_data.get("posts"):
            posts = validated_data.get("posts")
            i = 1
            for post in posts:
                models.Post.objects.create(**post, group=postgroup, order=i)
                i += 1

        return postgroup
