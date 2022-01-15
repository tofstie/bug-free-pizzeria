from django.db import models

# Create your models here.
class Book(AbstractBook):
    BookID = models.BigAutoField(primary_key=True)
    Title = models.CharField(max_length=255)
    Author = models.CharField(max_length=100)
    ISBN  = models.CharField(max_length=13)
    Edition = models.IntegerField()
    OriginalPrice = models.FloatField()
    AveragePrice = models.FloatField()
