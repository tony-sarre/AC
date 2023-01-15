from django.contrib.gis import admin
from django.shortcuts import render
from InformationSystem.models import (Alert, AlertList, counties)
from leaflet.admin import LeafletGeoAdmin


class AlertInline(admin.TabularInline):
    model = Alert
    extra = 0


@admin.register(AlertList)
class AlertListAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = (AlertInline,)
    pass


@admin.register(Alert)
class AlertAdmin(LeafletGeoAdmin ):
    list_display = ('title', 'autor', 'phone', 'due_date', 'location', 'Resolue', 'Encours')
    list_filter = ('due_date', 'Resolue', 'Encours')
    search_fields = ('title',)
#admin.site.register(Alert, AlertAdmin)


class countiesAdmin(LeafletGeoAdmin):
    list_display = ('counties', 'codes')


admin.site.register(counties, countiesAdmin)

