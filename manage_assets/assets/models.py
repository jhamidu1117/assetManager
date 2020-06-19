from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Asset(models.Model):
    Tag = models.CharField(max_length=100, blank=True)
    Serial_number = models.CharField(max_length=100, blank=True)
    Manufacturer = models.CharField(max_length=100, blank=True)
    asset_type = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.Tag


class Actions(models.Model):
    actor = models.ForeignKey(User, on_delete=models.CASCADE)
    target = models.ForeignKey(Asset, on_delete=models.CASCADE)
    action_log = models.CharField(max_length=100, blank=True)
    preformed_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.Tag

