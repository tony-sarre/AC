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
    path("dash_user/", views.incident, name="dash_user"),
    path("first/", views.first, name="index"),
    path("loginC/", views.User_profile, name="loginC"),
    path("login/", views.login, name="login"),
    path("login/", views.logout, name="logout"),
    path("Police_Profle/", views.Police_profile, name="Police_profile"),
    path("Gendarm_profile/", views.Gendarm_profile, name="Gendarm_profile"),
    path("Authority_profile/", views.Authority_profile, name="Authority_profile"),
    path("Fireman_profile/", views.Fireman_profile, name="Fireman_profile"),
    path("Rescuer_profile/", views.Rescuer_profile, name="Rescuer_profile"),
    path("Ong_profile/", views.Ong_profile, name="Ong_profile"),
    #path("citizen/profile/", views.citizen_profile, name='citizen_profile'),
    path("home/", views.home, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("user/", views.user, name="user"),
    path("table/", views.table, name="table"),
    path("template/", views.template, name="template"),
    path("typography/", views.typography, name="typography"),
    path("notifications/", views.notifications, name="notifications"),
    path("upgrade/", views.upgrade, name="upgrade"),
    path("icons/", views.icons, name="icons"),
    path("maps/", views.maps, name="maps"),
    path("long_running_task/", views.long_running_task, name="long_running_task"),
    #path("logout/", views.logout, name="logout"),
    path(r'county_data/', views.county_datasets, name = 'county'),
    path('Alert/', views.Alert, name= 'Alert'),
    path('save/<int:id>/', views.save, name='save'),
    path('print/<int:id>/', views.print, name='print'),
    path('Alert/<int:id>/', views.read, name='read'),

]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)