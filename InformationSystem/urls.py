# from django.urls import path, include
from rest_framework import routers
from InformationSystem import views
from InformationSystem.views import AlertViewSet, AlertListViewSet
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('alerts', AlertViewSet)
router.register('alert-lists', AlertListViewSet)

urlpatterns = [
    path("login/", views.login, name="login"),
    path("home/", views.home, name="home"),
    path("logout/", views.logout, name="logout"),
    path(r'^county_data/$', views.county_datasets, name = 'county'),
    path('Alert/', views.Alert, name= 'Alert'),
    path('save/<int:id>/', views.save, name='save'),
    path('print/<int:id>/', views.print, name='print'),
    path('Alert/<int:id>/', views.read, name='read'),

]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)