
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from docme.views import index

urlpatterns = [
    path("admin/", admin.site.urls),
    path(r'mdeditor/', include('mdeditor.urls')),
    path("docme/", include("docme.urls")),
    path("docs/", index),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
