from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models
#from django.contrib.gis.db.models import PointField
from django.db.models import Manager as GeoManager
# from django.contrib.gis import forms, gdal
from private_storage.fields import PrivateFileField


class Alert(models.Model):
    title = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    due_date = models.DateField()
    location = models.PointField(null=True, default=None, srid=4326)
    objects = GeoManager()
    Resolue = models.BooleanField()
    Encours = models.BooleanField()
    attachment = models.FileField(upload_to='public', null=True)
    private_file = PrivateFileField(upload_to='private', null=True)
    #labels = models.CharField(max_length=255)
    #sizes = models.CharField(max_length=255)

    list = models.ForeignKey('AlertList', null=False, on_delete=models.CASCADE)


class AlertList(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Alert List'
        verbose_name_plural = 'Alert Lists'


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


#class PieChartModel(models.Model):
 #   labels = models.CharField(max_length=255)
  #  sizes = models.CharField(max_length=255)

