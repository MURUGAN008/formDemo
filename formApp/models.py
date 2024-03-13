from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Notes(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE)

