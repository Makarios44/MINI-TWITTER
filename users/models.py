from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    email = models.EmailField()  # Campo de email
    first_name = models.CharField(max_length=30)  # Primeiro nome
    last_name = models.CharField(max_length=30)  # Último nome

    def __str__(self):
        return self.user.username

