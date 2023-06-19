from django.shortcuts import render
from rest_framework import generics
from django.db.models import Prefetch
from . import models, serializers


def index(request):
    return render(request, "docme/index.html")


class DocsApiView(generics.ListAPIView):
    # queryset = models.PostGroup.objects.all()
    queryset = models.PostGroup.objects.prefetch_related(Prefetch(
        "posts", models.Post.objects.order_by("order")))
    serializer_class = serializers.PostGroupSerializer


class RetrieveDocsPostApiView(generics.RetrieveAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    lookup_field = "slug"
