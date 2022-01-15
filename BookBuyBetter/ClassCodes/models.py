from django.db import models
from Book.models import Book;

# Create your models here.
class Book(models.Model):
    ClassCode = models.CharField(max_length=10,primary_key=True)
    Faculty = models.CharField(max_length=255)
    Department = models.CharField(max_length=100)
    BookID  = models.ForeignKey(Book, on_delete=models.DO_NOTHING, null = True)
