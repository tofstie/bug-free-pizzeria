from django.shortcuts import render, redirect

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
    all_listings = BookListing.objects.filter(Sold=False).order_by('DateAdded')
    paginator = Paginator(all_listings, 20)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {'page':page}
    return render(request, 'BookListings/all_listings.html', context)

def new_listing(request):
    if request.method != "POST":
        form = NewListingForm(initial={'Seller': request.user.email, 'DateAdded': datetime.datetime.today()})
    else:
        post = request.POST.copy()
        post['Seller'] = request.user
        post['DateAdded'] = datetime.datetime.today()
        request.POST = post

        form = NewListingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('BookListings:all_listings')

    context = {'form': form}
    return render(request, 'BookListings/new_listing.html', context)
