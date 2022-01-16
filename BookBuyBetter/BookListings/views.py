from django.shortcuts import render
from .models import BookListing
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    return render(request, 'BookListings/index.html')

def bookListingView(request):
    context = {'potato':'good'}
    BookListing.objects.get()
    return render(request, 'BookListings/bookListingView.html', context)

def all_listings(request):
    all_listings = BookListing.objects.filter(Sold=False).order_by('DateAdded')
    paginator = Paginator(all_listings, 20)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {'page':page}
    return render(request, 'BookListings/all_listings.html', context)
