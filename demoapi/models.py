from django.db import models


# Create your models here.

class DemoUsers(models.Model):
    username = models.CharField(max_length=255)
    age = models.IntegerField()
