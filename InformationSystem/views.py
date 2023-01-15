from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as dj_login, logout

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from django.core.serializers import serialize
from django.http import HttpResponse

from InformationSystem.models import Alert, AlertList, counties
from InformationSystem.serializers import AlertSerializer, AlertListSerializer, AlertListDetailSerializer
from .utils import get_plot

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            dj_login(request, user)
            return redirect("home")
        else:
            messages.info(request, "username or password is incorrect")

    context = {}
    return render(request, "login.html", context)


def logout(request):
    logout(request)
    return redirect("login")


@login_required(login_url="login")
def home(request):
    list_alert = Alert.objects.all()
    x = [x.location for x in list_alert]
    y = [y.title for y in list_alert]
    chart = get_plot(x, y)
    context = {"liste_alert": list_alert}
    return render(request, "index.html", context, {'chart': chart})


class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    permission_classes = (IsAuthenticated,)
    filterset_fields = ['due_date', 'Resolue', 'Encours']
    search_fields = ['title']

    @swagger_auto_schema(operation_description="This method returns a list of Alerts")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class AlertListViewSet(viewsets.ModelViewSet):
    queryset = AlertList.objects.all()
    serializer_class = AlertListSerializer
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return AlertListDetailSerializer
        return AlertListSerializer



def county_datasets(request):
    Counties = serialize('geojson', counties.objects.all())
    return HttpResponse(Counties,content_type='json')


def point_datasets(request):
    points = serialize('geojson', Alert.objects.all())
    return HttpResponse(points,content_type='json')


def save(request, id):
    # print('yes we are in edit file')
    alert = Alert.objects.get(id=id)
    if request.method == 'POST':
        alert_form = Alert(data=request.POST, instance=alert)
        if alert_form.is_valid():
            alert = alert_form.save()
            # print(student)
            return redirect('home')
    form = Alert(instance=alert)
    return render(request, 'main/save.html', {'alert_form': form, 'alert': alert})


def print(request, id):
    print(id)
    alert = Alert.objects.get(id=id)
    alert.print()
    #return redirect('home')
    return render(request, 'main/print.html', {'alert': alert})


def read(request, id):
    alert = Alert.objects.get(id=id)
    return render(request, 'main/read.html', {'alert': alert})