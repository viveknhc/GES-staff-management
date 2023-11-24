from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = ([
    path("admin/", admin.site.urls),
    path("", include("official.urls", namespace="official")),
    path("checker/", include("checker.urls", namespace="checker")),
    path("detailer/", include("detailer.urls", namespace="detailer")),

]

+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

)

admin.site.site_header = "Global Management Administration"
admin.site.site_title = "Global Management Admin Portal"
admin.site.index_title = "Welcome to Global Management Admin Portal"
