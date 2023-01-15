from django.shortcuts import render

from django.contrib.auth.models import User
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from user_management.serializers import UserSerializer


class MeViewSet(viewsets.ViewSet):

    permission_classes = (IsAuthenticated, )

    @swagger_auto_schema(
        operation_description='This method returns the user object that corresponds to the current user',
        responses={200: UserSerializer}
    )
    def list(self, request):

        user = User.objects.get(username=request.user)
        user_data = UserSerializer(user).data
        return Response(user_data)


