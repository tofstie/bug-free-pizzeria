from django.shortcuts import render
from .models import BookListing

# Create your views here.
def index(request):
    BookListing.objects.all()
    bookList = {}



    context = bookList
    return render(request, 'BookListings/index.html', context)

def bookListingView(request):


    return render(request, 'BookListings/bookListingView.html')