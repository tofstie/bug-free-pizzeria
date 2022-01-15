from django.db import models
from Books.models import Book
from Users.models import User

# Create your models here.
class BookListing(models.Model):
    ClassCode = models.CharField(max_length=10,primary_key=True)
    Faculty = models.CharField(max_length=255)
    Department = models.CharField(max_length=100)
    BookID  = models.ForeignKey(Book, on_delete=models.DO_NOTHING, null = True)