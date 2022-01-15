from django.db import models
from Books.models import Book;

# Create your models here.
class ClassCode(models.Model):
    ClassName = models.CharField(max_length=10,primary_key=True)
    Faculty = models.CharField(max_length=255)
    Department = models.CharField(max_length=100)
    BookID  = models.ForeignKey(Book, on_delete=models.DO_NOTHING, null = True)
