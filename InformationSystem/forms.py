#import geolocator as geolocator
from django import forms
from .models import Alert, UserProfile, PoliceProfile, GendarmProfile, FiremanProfile, AuthorityProfile, OngProfile, RescuerProfile
#from location_field.forms.plain import PlainLocationField


class AlertCreateForm(forms.ModelForm):
    class Meta:
        model = Alert
        fields = ['title', 'autor', 'phone', 'due_date', 'city', 'location', 'Resolue', 'Encours']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise forms.ValidationError('This field is required')
        for instance in Alert.objects.all():
            if instance.title == title:
                raise forms.ValidationError(title + 'is already added')
        return title

    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')
        if not due_date:
            raise forms.ValidationError('This field is required')
        return due_date


    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone:
            raise forms.ValidationError('This field is required')
        return phone

    def clean_city(self):
        city = self.cleaned_data.get('city')
        if not city:
            raise forms.ValidationError('This field is required')
        return city


class AlertUpdateForm(forms.ModelForm):
    class Meta:
        model = Alert
        fields = ['title', 'autor', 'phone', 'due_date', 'city']


class AlertSearchForm(forms.ModelForm):
    export_to_CSV = forms.BooleanField(required=False)
    due_date = forms.DateTimeField(required=False)

    class Meta:
        model = Alert
        fields = ['title', 'autor', 'phone', 'due_date', 'city']


class NumberAlertForm(forms.ModelForm):
    class Meta:
        model = Alert
        fields = ['number_alerts']


class ReceiveForm(forms.ModelForm):

    class Meta:
        model = Alert
        fields = ['receive_by']


class ResolueForm(forms.ModelForm):
    class Meta:
        model = Alert
        fields = ['Resolue']


class EncoursForm(forms.ModelForm):
    class Meta:
        model = Alert
        fields = ['Encours']


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
        ('--------', '---------'),
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


class PointForm(forms.Form):
    latitude = forms.FloatField()
    longitude = forms.FloatField()