from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from rest_framework import viewsets,permissions
from lolo.models import Book, BookJournalBase, Journal
from lolo.serializers import BookJournalBaseSerializer, BookSerializer, JournalSerializer

from appusers.permissions import IsOwnerOrReadOnly
from django.shortcuts import render



class BookViewSet(viewsets.ModelViewSet):
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BookViewSet_detail(viewsets.ModelViewSet):
   
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]


class JournalViewSet(viewsets.ModelViewSet):
    
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class JournalViewSet_detail(viewsets.ModelViewSet):
   
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]