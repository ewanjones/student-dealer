from django.db import models
from django.utils.timezone import now

class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField()
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    area = models.CharField(max_length=50)
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.id


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
