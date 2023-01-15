"""AlertCriminal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers, permissions

from InformationSystem.urls import router as InformatonSystem_router
from user_management.urls import router as user_management_router
import private_storage.urls

schema_view = get_schema_view(
   openapi.Info(
      title="Alert API",
      default_version='v1',
      description="This API is used to manage alerts",
      contact=openapi.Contact(email="contact@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=False,
   permission_classes=[permissions.AllowAny],
)


schema_view = get_schema_view(
   openapi.Info(
      title="Alert API",
      default_version='v1',
      description="This API is used to manage alerts",
      contact=openapi.Contact(email="contact@simpletech.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=False,
   permission_classes=[permissions.AllowAny],
)


router = routers.DefaultRouter()
router.registry.extend(InformatonSystem_router.registry)
router.registry.extend(user_management_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('InformationSystem/', include("InformationSystem.urls")),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('', include("InformationSystem.urls")),
    path('', include(router.urls)),
    re_path('^private-media/', include(private_storage.urls)),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
