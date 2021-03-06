from django.db import models
from Books.models import Book
from django.conf import settings
from django.utils.timezone import now

# Create your models here.
class BookListing(models.Model):
    ListingID = models.BigAutoField(primary_key=True)
    Seller =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Book =  models.ForeignKey(Book, on_delete=models.CASCADE)
    ListPrice = models.FloatField()
    DateAdded = models.DateTimeField(default=now)
    Sold = models.BooleanField(default=False)
    BookImage = models.ImageField(null=True, blank = True)

    def __str__(self):
        return str(self.Book) + ' ' + str(self.Seller)