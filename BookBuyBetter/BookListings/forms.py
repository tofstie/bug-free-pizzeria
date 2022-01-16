from importlib.machinery import FileFinder
from nntplib import ArticleInfo
from .models import BookListing, Book
from django.forms import ModelForm
from django import forms

class NewListingForm(ModelForm):
    class Meta:
        model = BookListing
        fields = ['Book', 'ListPrice', 'Seller', 'BookImage']
        labels = {'Book': 'Book', 'ListPrice': 'Price'}

