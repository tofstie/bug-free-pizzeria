from django.shortcuts import render, redirect
from .filters import ListingFilter
from .forms import NewListingForm
from .models import BookListing
from django.core.paginator import Paginator
import datetime

# Create your views here.
def index(request):
    return render(request, 'BookListings/index.html')

def bookListingView(request):
    context = {'potato':'good'}
    BookListing.objects.get()
    return render(request, 'BookListings/bookListingView.html', context)

def all_listings(request):
    sorting_option = request.GET['sort_by']
    if sorting_option == 'Highest Price':
        sorting = '-ListPrice'
    elif sorting_option == 'Lowest Price':
        sorting = 'ListPrice'
    else:
        sorting = "-DateAdded"
    all_listings = BookListing.objects.filter(Sold=False).order_by(sorting)
    
    my_Filter = ListingFilter(request.GET, queryset=all_listings)
    all_listings = my_Filter.qs
    paginator = Paginator(all_listings, 20)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    
    context = {'page':page, 'my_Filter': my_Filter}
    return render(request, 'BookListings/all_listings.html', context)

def new_listing(request):
    if request.method != "POST":
        form = NewListingForm()

    else:
        post = request.POST.copy()
        post['Seller'] = request.user
        request.POST = post

        form = NewListingForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('BookListings:all_listings')

    context = {'form': form}
    return render(request, 'BookListings/new_listing.html', context)

def listing(request, listing_id):
    listing_obj = BookListing.objects.get(ListingID=listing_id)
    context = {'listing_obj':listing_obj}
    return render(request, 'BookListings/listing.html', context)