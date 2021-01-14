from django.contrib.auth.models import User
from django.db import models


class Provider(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=1024)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"
