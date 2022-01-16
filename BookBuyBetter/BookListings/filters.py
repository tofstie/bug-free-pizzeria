import django_filters
from django_filters.widgets import RangeWidget
from .models import BookListing

class ListingFilter(django_filters.FilterSet):
    Book__Title = django_filters.CharFilter(lookup_expr='icontains')
    DateAdded = django_filters.DateRangeFilter(label='date')
    class Meta:
        model = BookListing
        fields = ['Book__Title', 'DateAdded']
