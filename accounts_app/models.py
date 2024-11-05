from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField(null=True, blank=True)
    tel = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.user.username

