from email import message
from statistics import mode
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class submit(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.CharField(max_length=255)
    dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fname


class posts(models.Model):

    full_name = models.CharField(max_length=50, null=True)
    category = models.CharField(max_length=200, null=True)
    season = models.CharField(max_length=200, null=True)
    stream_duration = models.CharField(max_length=255)
    episodes = models.CharField(max_length=200, null=True)
    mode_category = models.CharField(max_length=200, null=True)
    streaming_platform = models.CharField(max_length=200, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
