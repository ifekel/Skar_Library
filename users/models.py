from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    date_registered = models.DateTimeField(auto_now_add=True)   
    date_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.username