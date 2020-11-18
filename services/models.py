from django.db import models
from django.contrib.auth.models import User

class Service(models.Model):
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=1024)
    price = models.DecimalField(decimal_places=2)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
