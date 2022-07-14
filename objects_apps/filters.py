from django_filters import rest_framework as filters
from .models import *

class WatchListFilter(filters.FilterSet):
    
    name = filters.CharFilter(lookup_expr='iexact')
    type = filters.CharFilter(lookup_expr='iexact')
    
    platform_id = filters.NumberFilter(field_name='platform')
    platform_id__gt = filters.NumberFilter(field_name='platform',lookup_expr='gt')
    platform_id__lt = filters.NumberFilter(field_name='platform_id',lookup_expr='lt')
    platform__name = filters.CharFilter(field_name='platform__name',lookup_expr='icontains')
    
    created_at__year = filters.NumberFilter(field_name='created_at', lookup_expr='year')
    created_at__year_gt = filters.NumberFilter(field_name='created_at', lookup_expr='year__gt')
    created_at__year_lt = filters.NumberFilter(field_name='created_at', lookup_expr='year__lt')
    
    
    class Meta:
        model = WatchList
        fields = ['platform','type','name','created_at']