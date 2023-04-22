from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import csv
from django.contrib.auth import authenticate, login as dj_login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from drf_yasg.utils import swagger_auto_schema
from geopy import Location
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from django.core.serializers import serialize

from InformationSystem.models import Alert, AlertList, counties, UserProfile, AuthorityProfile, PoliceProfile,GendarmProfile,OngProfile, FiremanProfile, RescuerProfile
from InformationSystem.serializers import AlertSerializer, AlertListSerializer, AlertListDetailSerializer
from .utils import get_plot, get_plot2, generate_pie_chart, plot_view
#from location_field.functions import reverse_geocode
from .forms import IncidentForm, UserProfileAdmin, PoliceProfileAdmin, OngProfileAdmin, FiremanProfileAdmin, \
    GendarmProfileAdmin, RescuerProfileAdmin, AuthorityProfileAdmin, LoginForm, AlertCreateForm, AlertSearchForm, \
    AlertUpdateForm, NumberAlertForm, ReceiveForm, ResolueForm, EncoursForm
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import numpy as np
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib import messages
from geopy.geocoders import Nominatim
import joblib


def predict_crime(request):
    # load the saved model
    model = joblib.load('AlertList')

    # get the input data from the request
    input_data = request.GET

    # convert the input data into a format suitable for the model
    # e.g., convert categorical data into numerical data

    # make a prediction using the model
    prediction = model.predict(input_data)

    # return the prediction as a JSON response
    return JsonResponse({'prediction': prediction})



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


def loginC(request):
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
    return render(request, "loginC.html", context)


def User_profile(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        form = UserProfileAdmin(request.POST)
        if user is not None and user.is_User and form.is_valid():
            login(request, user)
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('home')
    else:
        messages.error(request, 'Invalid username or password.')
        form = UserProfileAdmin()
    return render(request, 'loginC.html', {'form': form})


def Police_profile(request):
    if request.method == 'POST':
        MatriculeP = request.POST['matriculeP']
        CompanyNameP = request.POST['company_nameP']
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, CompanieName=CompanyNameP, id=MatriculeP, username=username, password=password)
        form = PoliceProfileAdmin(request.POST)
        if user is not None and user.is_Police_Profile and form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect(request, 'index.html', {'form': form})
    else:
        messages.error(request, 'Invalid username or password.')
        form = PoliceProfileAdmin()
    return render(request, 'login.html', {'form': form})


def Gendarm_profile(request):
    if request.method == 'POST':
        MatriculeG = request.POST['matriculeG']
        CompanyNameG = request.POST['company_nameG']
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, CompanieName=CompanyNameG, id=MatriculeG, username=username, password=password)
        form = GendarmProfileAdmin(request.POST)
        if user is not None and user.is_Gendarm_Profile and form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect(request, 'index.html', {'form': form})
    else:
        messages.error(request, 'Invalid username or password.')
        form = GendarmProfileAdmin()
    return render(request, 'login.html', {'form': form})


def Fireman_profile(request):
    if request.method == 'POST':
        MatriculeF = request.POST['matriculeF']
        CompanyNameF = request.POST['company_nameF']
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, CompanieName=CompanyNameF, id=MatriculeF, username=username, password=password)
        form = FiremanProfileAdmin(request.POST)
        if user is not None and user.is_Fireman_Profile and form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect(request, 'index.html', {'form': form})
    else:
        messages.error(request, 'Invalid username or password.')
        form = FiremanProfileAdmin()
    return render(request, 'login.html', {'form': form})


def Rescuer_profile(request):
    if request.method == 'POST':
        MatriculeR = request.POST['matriculeR']
        CompanyNameR = request.POST['company_nameR']
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, CompanieName=CompanyNameR, id=MatriculeR, username=username, password=password)
        form = RescuerProfileAdmin(request.POST)
        if user is not None and user.is_Rescuer_Profile and form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect(request, 'index.html', {'form': form})
    else:
        messages.error(request, 'Invalid username or password.')
        form = RescuerProfileAdmin()
    return render(request, 'login.html', {'form': form})


def Authority_profile(request):
    if request.method == 'POST':
        MatriculeA = request.POST['matriculeA']
        #CompanieName = request.POST['CompanieName']
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, id=MatriculeA, username=username, password=password)
        form = AuthorityProfileAdmin(request.POST)
        if user is not None and user.is_Authority_Profile and form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect(request, 'index.html', {'form': form})
    else:
        messages.error(request, 'Invalid username or password.')
        form = AuthorityProfileAdmin()
    return render(request, 'login.html', {'form': form})


def Ong_profile(request):
    if request.method == 'POST':
        #Matricule = request.POST['Matricule']
        CompanyNameO = request.POST['company_nameO']
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, CompanieName=CompanyNameO, username=username, password=password)
        form = OngProfileAdmin(request.POST)
        if user is not None and user.is_Ong_Profile and form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect(request, 'index.html', {'form': form})
    else:
        messages.error(request, 'Invalid username or password.')
        form = OngProfileAdmin()
    return render(request, 'login.html', {'form': form})


def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.profile.profile_type == "PoliceProfile":
                return redirect("admin_profile")
            elif user.profile.profile_type == "UserProfile":
                return redirect("User_profile")
    return render(request, "login.html", {"form": form})


def logout(request):

    return redirect('login')


@login_required(login_url="login")
def home(request):
    header = 'List of alerts'
    form = AlertSearchForm(request.POST or None)
    queryset = Alert.objects.all()
    context = {
        "header": header,
        "queryset": queryset,
        "form": form,
    }
    if request.method == 'POST':
        queryset = Alert.objects.filter(title__icontains=form['title'].value(),
                                        due_date__icontains=form['due_date'].value(),
                                        city__icontains=form['city'].value(),

                                        )

        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="List of alert.csv"'
            writer = csv.writer(response)
            writer.writerow(['title', 'autor', 'phone', 'due_date', 'city', 'location', 'Resolue', 'Encours'])
            instance = queryset
            for alert in instance:
                writer.writerow([alert.title, alert.autor, alert.phone, alert.due_date, alert.city, alert.location, alert.Resolue, alert.Encours])
            return response
        context = {
            "form": form,
            "header": header,
            "queryset": queryset,
        }
    return render(request, "index.html", context)


@login_required(login_url="login")
def first(request):

    #list_alert = Alert.objects.all()
   # context = {"liste_alert": list_alert}
    return render(request, "first.html")

#@login_required(login_url="login")
def dashboard(request):
    data={}
    entry=vars()
    list_alert = Alert.objects.all()
    x = [x.location for x in list_alert]
    y = [y.title for y in list_alert]
    #z = [z.location for z in list_alert]
    X = [X.due_date for X in list_alert]
    Y = [Y.title for Y in list_alert]
   # Z = [Z.due_date for Z in list_alert]
    n=[n.title for n in list_alert]
    for entry in list_alert:
        data[entry.title] = entry.Encours
    image_file = generate_pie_chart(data)
    figdata_png = plot_view(n)
    chart = get_plot(x, y)
    charti= get_plot2(X, Y)
    context = {'chart': chart, 'charti': charti, 'image_file': image_file, 'figdata_png':figdata_png}
    #return HttpResponse(image_file.read(), content_type="image/png")

    return render(request, "dashboard.html", context)


def user(request):
    return render(request, "user.html")


def table(request):
    header = 'List of alerts'
    queryset = Alert.objects.all()
    form = AlertSearchForm(request.POST or None)
    context = {
        "header": header,
        "queryset": queryset,
    }

    if request.method == 'POST':
        t = form['title'].value()
        queryset = Alert.objects.filter(
            city__icontains=form['city'].value()
        )

        if (t != ''):
            queryset = queryset.filter(title_id=t)

        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="Alert History.csv"'
            writer = csv.writer(response)
            writer.writerow(['title', 'autor', 'phone', 'due_date', 'city', 'location', 'Resolue', 'Encours'])
            instance = queryset
            for alert in instance:
                writer.writerow(
                    [alert.title, alert.autor, alert.phone, alert.due_date, alert.city, alert.location, alert.Resolue,
                     alert.Encours])

                return response

        context = {
            "form": form,
            "header": header,
            "queryset": queryset,
        }

    return render(request, "table.html", context)


def add_alert(request):
    form = AlertCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully Saved')
        return redirect('home')
    context = {
        "form": form,
        "title": "Add Alert",
    }
    return render(request, "add_alert.html", context)


def update_alert(request, pk):
    queryset = Alert.objects.get(id=pk)
    form = AlertUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = AlertUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Saved')
            return redirect('home')

    context = {
        'form': form
    }
    return render(request, 'add_alert.html', context)


def delete_alert(request, pk):
    queryset = Alert.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        messages.success(request, 'Delete Successfully')
        return redirect('home')
    return render(request, 'delete_alert.html')


def alert_detail(request, pk):
    queryset = Alert.objects.get(id=pk)
    context = {
        #"title": queryset.title,
        "queryset": queryset,
    }
    return render(request, "main/read.html", context)


def number_alert(request, pk):
    queryset = Alert.objects.get(id=pk)
    form =NumberAlertForm(request.POST or None, instance=queryset)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.number_alerts -= 1
        #instance.issue_by = str(request.user)
        messages.success(request, " SUCCESSFULLY. " + str(instance.title) + " " + str(instance.city) + "s now left in Store")
        instance.save()

        return redirect('/alert_detail/'+str(instance.id))
        # return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": 'City' + str(queryset.city),
        "queryset": queryset,
        "form": form,
        #"username": 'Issue By: ' + str(request.user),
    }
    return render(request, "add_alert.html", context)


def receive_alerts(request, pk):
    queryset = Alert.objects.get(id=pk)
    form = ReceiveForm(request.POST or None, instance=queryset)
    if form.is_valid():
        instance = form.save(commit=False)
        #instance.receive_by += instance.receive
        instance.save()
        messages.success(request, "Received SUCCESSFULLY. " + str(instance.title) + " " + str(instance.city)+"s now in Store")

        return redirect('/alert_detail/'+str(instance.id))
        # return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": 'Receive ' + str(queryset.receive),
        "instance": queryset,
        "form": form,
        "username": 'Receive By: ' + str(request.user),
    }
    return render(request, "add_alert.html", context)


def Resolue(request, pk):
    queryset = Alert.objects.get(id=pk)
    form = ResolueForm(request.POST or None, instance=queryset)
    Form = EncoursForm(request.POST or None, instance=queryset)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Resolue for " + str(instance.title) + " is updated to " + str(instance.Resolue))
        return redirect("/home")
    elif Form.is_valid():
        instance = Form.save(commit=False)
        instance.save()
        messages.success(request, "Encours for " + str(instance.title) + " is updated to " + str(instance.Encours))
        return redirect("/home")

    context = {
            "instance": queryset,
            "form": form,
            "Form": Form,
        }
    return render(request, "add_alert.html", context)


def typography(request):
    return render(request, "typography.html")


def notifications(request):
    return render(request, "notifications.html")


def template(request):
    return render(request, "template.html")


def upgrade(request):
    return render(request, "upgrade.html")


def icons(request):
    return render(request, "icons.html")


def maps(request):
    return render(request, "maps.html")



#def add_location(request):
    # Get the latitude and longitude from the request
    #latitude = request.POST['14.497401']
    #longitude = request.POST['-14.452362']

    # Use the geocoding API to get the city name
    #geolocator = Nominatim(user_agent='InformationSystem')
    #Location = geolocator.reverse(f"{latitude}, {longitude}")
    #city = Location.raw['address']['city']

    # Create a new Location object and save it to the database
    #Location = Alert(latitude=latitude, longitude=longitude, city=city)
    #Location.save()

   # return HttpResponse("Location added successfully")


#def view_location(request, location_id):
 #   location = Location.objects.get(id=location_id)
  #  return HttpResponse(f"This location is in {location.city}")



def map_view(request):
   # locations = [
    #    {'latitude': 14.6919,'longitude': -17.4474,"name":"Dakar"},
     #   {"latitude":16.237997,'longitude': -16.212559,"name": "Saint-Louis"},
    #]
    #return render(request, 'main/read.html', {'locations': locations})if request.method == 'POST':
    lat = request.POST.get('lat')
    lng = request.POST.get('lng')

        # Perform any necessary processing
    data = [{'lat': lat + 0.1, 'lng': lng + 0.1}, {'lat': lat - 0.1, 'lng': lng - 0.1}]

    return JsonResponse(data, safe=False)


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


#def read(request, id):
 #   alert = Alert.objects.get(id=id)
  #  return render(request, 'main/read.html', {'alert': alert})


def incident(request):
    if request.method == 'POST':
        form = IncidentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            latitude = form.cleaned_data['latitude']
            longitude = form.cleaned_data['longitude']
            geolocator = Nominatim(user_agent="InformationSystem")
            location = geolocator.reverse(f"{latitude}, {longitude}")
            address = location.address
            messages.success(request, f"GPS location: {location.address}")
            #city = location.raw['address']['city']

            # Create a new Location object and save it to the database
            #Location = Alert(latitude=latitude, longitude=longitude, city=city)
            #Location.save()

    else:
        form = IncidentForm()
    return render(request, 'dash_user.html', {'form': form})


#def view_location(request, location_id):
 #   location = Location.objects.get(id=location_id)
  #  return HttpResponse(f"This location is in {location.city}")





def long_running_task(request):
    # Perform the long-running task
    progress = 0
    while progress < 100:
        # Update the progress of the task
        progress += 10

    # Return the progress as a JSON response
    return JsonResponse({'progress': progress})