from django.contrib.auth.models import User
from rest_framework import serializers

from user_management.models import AlertUserProfile


class AlertUserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = AlertUserProfile
        fields = ('phone', 'lucky_number')


class UserSerializer(serializers.ModelSerializer):

    profile = AlertUserProfileSerializer(source='alertuserprofile')

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email','profile')
