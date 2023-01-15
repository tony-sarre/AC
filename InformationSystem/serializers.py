from rest_framework import serializers

from InformationSystem.models import Alert, AlertList


class AlertSerializer(serializers.ModelSerializer):

    dueDate = serializers.DateField(source='due_date')

    class Meta:
        model = Alert
        exclude = ['due_date']


class AlertListSerializer(serializers.ModelSerializer):

    class Meta:
        model = AlertList
        fields = '__all__'


class AlertListDetailSerializer(serializers.ModelSerializer):
    Alert = AlertSerializer(source='alert_set', many=True)

    class Meta:
        model = AlertList
        fields = '__all__'
