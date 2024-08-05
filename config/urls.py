from django.contrib import admin
from django.urls import path
from django.conf import settings
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="My Learning System API",
        default_version="v1",
        description="An Learning System API for Me",
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path(settings.ADMIN_URL, admin.site.urls),
]

admin.site.site_header = "My Learning System"
admin.site.site_title = "My Learning System Admin Portal"
admin.site.index_title = "Welcome to My Learning Systems Portal"
