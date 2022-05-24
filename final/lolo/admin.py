from django.contrib import admin

from lolo.models import Book, BookJournalBase, Journal

# Register your models here.

admin.site.register(Book)
admin.site.register(Journal)