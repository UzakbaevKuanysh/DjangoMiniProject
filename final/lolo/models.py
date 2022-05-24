from django.db import models

# Create your models here.
class BookJournalBase(models.Model):
    owner = models.ForeignKey('auth.User',related_name='bookjournalbase', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(blank=True)

    class Meta:
        abstract = True
class Book(BookJournalBase):
    owner = models.ForeignKey('auth.User',related_name='book', on_delete=models.CASCADE, null=True)
    num_pages = models.PositiveIntegerField()
    genre = models.CharField(max_length=100)
class Journal(BookJournalBase):
    types =  ('B', 'Bullet'),
    ('F', 'Food'),
    ('T', 'Travel'),
    ('S', 'Sport')
    type  = models.CharField(max_length=1, choices=types, default='B')
    publisher = models.CharField(max_length =100)

    