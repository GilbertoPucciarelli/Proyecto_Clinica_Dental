from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=255, default='Pacient')
    bloqued = models.BooleanField(default=False)
    

    def __str__(self):
        
        return self.user.username