from nntplib import ArticleInfo
from .models import BookListing, Book
from django.forms import ModelForm

class NewListingForm(ModelForm):
    class Meta:
        model = BookListing
        fields = ['Book', 'ListPrice', 'DateAdded']

