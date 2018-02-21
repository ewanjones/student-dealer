from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now

from django.contrib.auth.models import User

class Business(models.Model):
    id = models.AutoField(primary_key=True)
    # image = models.FileField()
    name = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    address = models.CharField(max_length=200)  # comma separated
    business_type = models.CharField(max_length=20)
    description = models.TextField()
    url = models.URLField()

    def __str__(self):
        return self.name


class Deal(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    code = models.CharField(max_length=50)

    def __str__(self):
        return self.id


class IPAddress(models.Model):
    ip = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
