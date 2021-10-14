import django_filters
from .models import Website

class CategoryFilter(django_filters.FilterSet):
    class Meta:
            model = Website
            fields = ['category']