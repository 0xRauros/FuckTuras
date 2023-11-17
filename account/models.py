from django.db import models
from django.conf import settings
from django.utils.html import mark_safe


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                related_name='profile',
                                on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',
                              blank=True)
    address = models.CharField(blank=True, max_length=200)
    city = models.CharField(blank=True, max_length=100)
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)
    

    def __str__(self):
        return f'Profile of {self.user.username}'

    def photo_field(self):
        if self.photo:
            return mark_safe(f"<img src='{self.photo.url}' width='100px;' height='50px;' />")
        return ''
    


class Settings(models.Model):
    profile = models.OneToOneField(Profile,
                                   related_name='settings',
                                   on_delete=models.CASCADE)
    primary_color = models.CharField(max_length=7, blank=True)
    secondary_color = models.CharField(max_length=7, blank=True)
    dark_mode = models.BooleanField(default=True)
