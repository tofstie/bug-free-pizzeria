from django.urls import path, include

from . import views

app_name = 'BookListings'

urlpatterns = [
    path('', views.index, name='index'),
    path('all_listings', views.all_listings, name='all_listings')
]