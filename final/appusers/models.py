from django.db import models

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AppUser(models.Model):
    owner = models.ForeignKey('auth.User',related_name='appuser', on_delete=models.CASCADE, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    USER_TYPES = (
    ('S', 'SuperAdmin'),
    ('G', 'Guest')
    )
    
    
    user_type = models.CharField(max_length=1, choices=USER_TYPES, default='C')
    
    mobile = models.PositiveIntegerField(null=True, blank=True)
    address = models.CharField(max_length=500, null=True,blank=True)
    city = models.CharField(max_length=250,null=True,blank=True)
    pincode = models.PositiveIntegerField(null=True,blank=True)

    def __str__(self):
        return self.user.username


