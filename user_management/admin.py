from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from user_management.models import AlertUserProfile


class AlertUserProfileInline(admin.StackedInline):

    model = AlertUserProfile


class AlertUserAdmin(UserAdmin):

    inlines = (AlertUserProfileInline, )


admin.site.unregister(User)
admin.site.register(User, AlertUserAdmin)

