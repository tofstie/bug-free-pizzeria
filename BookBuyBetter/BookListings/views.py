from django.shortcuts import render
from .models import BookListing

# Create your views here.
def index(request):
    return render(request, 'BookListings/index.html')

def bookListingView(request):
    context = {'potato':'good'}
    BookListing.objects.get()
    return render(request, 'BookListings/bookListingView.html', context)