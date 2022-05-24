from django.shortcuts import render

from appusers.models import AppUser
from appusers.serializers import AppUserSerializer
from rest_framework import viewsets,permissions

from appusers.permissions import IsOwnerOrReadOnly
# Create your views here.
class AppUserViewSet(viewsets.ModelViewSet):
    
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class AppUserViewSet_detail(viewsets.ModelViewSet):
   
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]