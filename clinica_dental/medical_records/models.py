from django.db import models
from django.contrib.auth.models import User

from users.models import Profile
from appointments.models import Consultations


class MedicalRecords(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    dni = models.CharField(max_length=10)
    age = models.CharField(max_length=3)
    birthday = models.DateField()
    marital_status = models.CharField(max_length=255)
    nacionality = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    user = models.OneToOneField(User, on_delete=models.CASCADE)


class AccountStatus(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=10, default='Pending')

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    consultation = models.ForeignKey(Consultations, on_delete=models.CASCADE)