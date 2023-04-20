from __future__ import unicode_literals
#from django.db import models
from django.contrib.gis.db import models
#from django.contrib.gis.db.models import PointField
from django.db.models import Manager as GeoManager
#from django.contrib.gis import forms, gdal
from private_storage.fields import PrivateFileField
from django.contrib.auth.models import User
#from geopy.geocoders import Nominatim
from django.contrib.gis.db import models as gis_models
from django.db import connection
# or if you're querying a non-default database:
from django.db import connections


class Location(models.Model):
    name = models.CharField(max_length=255)
    location = gis_models.PointField()
    others = models.CharField(max_length=255)


title_choice = (
        ('Agression', 'Agression'),
        ('Viol', 'Viol'),
        ('Omisside', 'Omisside'),
        ('Viole', 'Viole'),
        ('Incendie', 'Incendie'),
        ('Inondation', 'Inondation'),
)


class AlertList(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'Alert List'
        verbose_name_plural = 'Alert Lists'

    def __str__(self):
        return self.name


class Alert(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    autor = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    due_date = models.DateField(blank=True)
    location = models.PointField(null=True, default=None, srid=4326)
    objects = GeoManager()
    latitude = models.DecimalField(null=True, max_digits=9, decimal_places=6)
    longitude = models.DecimalField(null=True, max_digits=9, decimal_places=6)
    last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    Resolue = models.BooleanField(default=False)
    Encours = models.BooleanField(default=False)
    number_alerts = models.IntegerField(blank=True, null=True, default=0)
    receive = models.CharField(max_length=255, blank=True, null=True)
    receive_by = models.CharField(max_length=255, blank=True, null=True)


    attachment = models.FileField(upload_to='public', null=True)
    private_file = PrivateFileField(upload_to='private', null=True)
    #labels = models.CharField(max_length=255)
    #sizes = models.CharField(max_length=255)

    list = models.ForeignKey('AlertList', null=False, on_delete=models.CASCADE)
    city = models.CharField(null=True, max_length=100, blank=True)

    def __str__(self):
        return self.title


class counties(models.Model):
    counties = models.CharField(max_length=25)
    codes = models.IntegerField()
    cty_code = models.CharField(max_length=24)
    dis = models.IntegerField()
    geom = models.MultiPolygonField(null=True, default=None, srid=4326)

    def __unicode__(self):
        return self.counties
    class Meta:
        verbose_name_plural = 'Counties'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'User'


class PoliceProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_nameP = models.CharField(max_length=100)
    matriculeP = models.CharField(max_length=100, primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Police'
        verbose_name_plural = 'Police'


class AuthorityProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #company_name = models.CharField(max_length=100)
    matriculeA = models.CharField(max_length=100, primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Authority'
        verbose_name_plural = 'Authority'


class OngProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_nameO = models.CharField(max_length=100, primary_key=True)
    #matricule = models.CharField(max_length=100, primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Ong'
        verbose_name_plural = 'Ong'


class GendarmProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_nameG = models.CharField(max_length=100)
    matriculeG = models.CharField(max_length=100, primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Gendarm'
        verbose_name_plural = 'Gendarm'


class FiremanProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_nameF = models.CharField(max_length=100)
    matriculeF = models.CharField(max_length=100, primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Fireman'
        verbose_name_plural = 'Fireman'


class RescuerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_nameR = models.CharField(max_length=100)
    matriculeR = models.CharField(max_length=100, primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Rescuer'
        verbose_name_plural = 'Rescuer'



#class PieChartModel(models.Model):
 #   labels = models.CharField(max_length=255)
  #  sizes = models.CharField(max_length=255)


