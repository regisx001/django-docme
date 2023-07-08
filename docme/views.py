from django.shortcuts import render
from rest_framework import generics
from django.db.models import Prefetch
from . import models, serializers


def index(request):
    return render(request, "docme/index.html")


class DocsApiView(generics.ListCreateAPIView):
    queryset = models.PostGroup.objects.prefetch_related(Prefetch(
        "posts", models.Post.objects.order_by("order")))
    serializer_class = serializers.PostGroupSerializer


class DeletePostGroup(generics.RetrieveDestroyAPIView):
    queryset = models.PostGroup.objects.all()
    serializer_class = serializers.PostGroupSerializer
    lookup_field = "pk"


class CreatePostAPIView(generics.CreateAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer


class RetrieveDocsPostApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    lookup_field = "slug"
