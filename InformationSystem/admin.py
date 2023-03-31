from django.contrib.gis import admin
from django.shortcuts import render
from InformationSystem.models import (Alert, AlertList, counties, PoliceProfile, AuthorityProfile, GendarmProfile, FiremanProfile, RescuerProfile, OngProfile)
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
# admin.site.register(Alert, AlertAdmin)



class CountiesAdmin(LeafletGeoAdmin):
    list_display = ('counties', 'codes')


admin.site.register(counties, CountiesAdmin)


@admin.register(PoliceProfile)
class PoliceProfileAdmin(admin.ModelAdmin):
    list_display = ('matriculeP', 'company_nameP', 'username')


@admin.register(GendarmProfile)
class GendarmProfileAdmin(admin.ModelAdmin):
    list_display = ('matriculeG', 'company_nameG', 'username')


@admin.register(AuthorityProfile)
class AuthorityProfileAdmin(admin.ModelAdmin):
    list_display = ('matriculeA', 'username')


@admin.register(FiremanProfile)
class FiremanProfileAdmin(admin.ModelAdmin):
    list_display = ('matriculeF', 'company_nameF', 'username')


@admin.register(RescuerProfile)
class RescuerProfileAdmin(admin.ModelAdmin):
    list_display = ('matriculeR', 'company_nameR', 'username')


@admin.register(OngProfile)
class OngProfileAdmin(admin.ModelAdmin):
    list_display = ('company_nameO', 'username')