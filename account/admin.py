from django.contrib import admin
from .models import Profile, Settings


class SettingsInline(admin.StackedInline):
    model = Settings

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'photo_field', 'settings']
    inlines = (SettingsInline, )

