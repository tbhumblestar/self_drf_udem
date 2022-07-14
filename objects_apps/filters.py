from django_filters import rest_framework as filters
from .models import *

class WatchListFilter(filters.FilterSet):
    
    name = filters.CharFilter(lookup_expr='iexact')
    type = filters.CharFilter(lookup_expr='iexact')
    
    platform_id = filters.NumberFilter(field_name='platform_id')
    platform_id__gt = filters.NumberFilter(field_name='platform_id',lookup_expr='gt')
    platform_id__lt = filters.NumberFilter(field_name='platform_id',lookup_expr='lt')
    
    platform__name = filters.CharFilter(field_name='platform__name',lookup_expr='icontains')
    
    
    class Meta:
        model = WatchList
        fields = ['platform_id','type','name',]