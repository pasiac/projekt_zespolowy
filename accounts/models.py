from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, int_list_validator

class BusinessProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nip = models.CharField(max_length=10, validators=[int_list_validator(sep=''),MinLengthValidator(10),])
    verified = models.BooleanField(default=False)

class CreditCard(models.Model):
    ### Zrobic z szyfrowaniem ###
    pass

class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
