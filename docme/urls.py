from django.urls import path
from . import views

urlpatterns = [
    # path("view/", views.index, name=""),
    path("", views.DocsApiView.as_view(),),
    path("<str:slug>/", views.RetrieveDocsPostApiView.as_view(),),
]
