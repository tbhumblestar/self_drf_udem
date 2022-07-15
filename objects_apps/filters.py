from django_filters import rest_framework as filters
from .models import *

class WatchListFilter(filters.FilterSet):
    
    # name = filters.CharFilter(lookup_expr='iexact')
    # type = filters.CharFilter(lookup_expr='iexact')
    
    # platform_id = filters.NumberFilter(field_name='platform')
    # platform_id__gt = filters.NumberFilter(field_name='platform',lookup_expr='gt')
    # platform_id__lt = filters.NumberFilter(field_name='platform_id',lookup_expr='lt')
    # platform__name = filters.CharFilter(field_name='platform__name',lookup_expr='icontains')
    
    # created_at__year = filters.NumberFilter(field_name='created_at', lookup_expr='year')
    # created_at__year_gt = filters.NumberFilter(field_name='created_at', lookup_expr='year__gt')
    # created_at__year_lt = filters.NumberFilter(field_name='created_at', lookup_expr='year__lt')
    
    
    class Meta:
        model = WatchList
        # fields = ['platform','type','name','created_at']
        
        #exact는 필드가 생기지 않는다. lt,gt등은 필드가 생김
        #created__Year
        fields = {
            #name필터가 생성이 됨
            'name':['exact'],
            'type':['exact'],
            
            #created_at__year이 기준이 됨
            #created_at__year / created_at__year__gt / created_at__year__lt 필터가 생김
            'created_at':['year','year__gt','year__lt'],
            
            'platform':['exact','lt','gt'],
            #platform__name__icontains필터가 생성됨
            'platform__name':['icontains']
        }