from rest_framework import serializers

from appusers.models import AppUser

class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ['user', 'owner', 'mobile','address', 'city', 'pincode', 'user_type']