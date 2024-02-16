from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    email = models.EmailField(blank=True)
    facebook_url = models.URLField(blank=True)
   

    def __str__(self):
        return self.user.username
