from django.db import models
from django.contrib.auth.models import User

from users.models import Profile


class WorkBlocks(models.Model):

    day = models.CharField(max_length=10)
    hour = models.CharField(max_length=10)
    doctor_name = models.CharField(max_length=255)

    doctor = models.ForeignKey(User, on_delete=models.CASCADE)


class Appointments(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=255)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    block = models.ForeignKey(WorkBlocks, on_delete=models.CASCADE)


class Consultations(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    block = models.ForeignKey(WorkBlocks, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointments, on_delete=models.CASCADE)

    price = models.IntegerField()
    medicaments = models.TextField()
    symtoms = models.TextField()
    treatment = models.TextField()
    payment = models.CharField(max_length=255)
