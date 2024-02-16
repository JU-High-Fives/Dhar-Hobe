from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    """
    Model representing a user profile.
    """

    # One-to-one relationship with the User model
    m_user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # User's bio
    m_bio = models.TextField(max_length=500, blank=True)
    
    # User's profile picture
    m_profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    
    # User's email
    m_email = models.EmailField(blank=True)
    
    # User's Facebook URL
    m_facebook_url = models.URLField(blank=True)

    def __str__(self):
        """
        String representation of the profile.
        """
        return self.user.username
