from rest_framework import serializers

from lolo.models import BookJournalBase, Book, Journal

class BookJournalBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookJournalBase
        fields = ['owner', 'name', 'price', 'created_at', 'description']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['num_pages','owner', 'genre']
        
class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = ['owner', 'publisher', 'type']
        