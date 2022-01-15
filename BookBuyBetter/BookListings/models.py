from django.db import models
from Books.models import Book
from Users.models import User

# Create your models here.
class BookListing(models.Model):
    ListingID = models.BigAutoField(primary_key=True)
    Seller =  models.ForeignKey(User, on_delete=models.CASCADE)
    Book =  models.ForeignKey(Book, on_delete=models.CASCADE)
    ListPrice = models.FloatField()
    DateAdded = models.DateTimeField()
    Sold = models.BooleanField()
    BookImage = models.ImageField()
