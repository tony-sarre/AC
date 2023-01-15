from rest_framework import routers

from user_management.views import MeViewSet

router = routers.DefaultRouter()
router.register('me', MeViewSet, basename='me')