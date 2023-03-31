#import geolocator as geolocator
from django import forms
from .models import UserProfile, PoliceProfile, GendarmProfile, FiremanProfile, AuthorityProfile, OngProfile, RescuerProfile
#from location_field.forms.plain import PlainLocationField

class UserProfileAdmin(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['address', 'phone_number']


class PoliceProfileAdmin(forms.ModelForm):
    class Meta:
        model = PoliceProfile
        fields = ['company_nameP', 'matriculeP']


class GendarmProfileAdmin(forms.ModelForm):
    class Meta:
        model = GendarmProfile
        fields = ['company_nameG', 'matriculeG']


class FiremanProfileAdmin(forms.ModelForm):
    class Meta:
        model = FiremanProfile
        fields = ['company_nameF', 'matriculeF']


class RescuerProfileAdmin(forms.ModelForm):
    class Meta:
        model = RescuerProfile
        fields = ['company_nameR', 'matriculeR']


class OngProfileAdmin(forms.ModelForm):
    class Meta:
        model = OngProfile
        fields = ['company_nameO']


class AuthorityProfileAdmin(forms.ModelForm):
    class Meta:
        model = AuthorityProfile
        fields = ['matriculeA']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class IncidentForm(forms.Form):


    name = [
        ('fill in here', 'fill in here'),
        ('Agression', 'Agression'),
        ('Viol', 'Viol'),
        ('Omisside', 'Omisside'),
        ('Viole', 'Viole'),
        ('Incendie', 'Incendie'),
        ('Inondation', 'Inondation'),
    ]
    Incident_name = forms.ChoiceField(choices=name)
    latitude = forms.DecimalField(max_digits=9, decimal_places=6, widget=forms.HiddenInput())
    longitude = forms.DecimalField(max_digits=9, decimal_places=6, widget=forms.HiddenInput())
    #name = forms.CharField(max_length=100)
    #location = forms.CharField(widget=forms.HiddenInput())
    Others = forms.CharField(widget=forms.Textarea)
    location = forms.CharField(widget=forms.Textarea)
    #address = location.address


def post(request):
    form = IncidentForm(request.POST)
    if form.is_valid():
        location = form.cleaned_data['latitude', 'longitude']
        return location


#class LocationForm(forms.Form):
 #   location = forms.CharField(widget=forms.HiddenInput())
