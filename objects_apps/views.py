from django.shortcuts import get_object_or_404

# Create your views here.
from rest_framework import generics
from objects_apps.models import *
from objects_apps.serializers import (
                                    StreamPlatformSerializer,
                                    WatchListSerializer,
                                    ReviewSerializer
                                    )
from rest_framework.permissions import (IsAuthenticated,IsAuthenticatedOrReadOnly)

from django_filters import rest_framework as filters

from objects_apps.permissions import IsAdminOrReadOnly
from objects_apps.pagination  import WatchListPagination, LOPagination, CPagination
from objects_apps.filters import WatchListFilter

class StreamPlatformView(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = StreamPlatformSerializer
    queryset = StreamPlatform.objects.all()


class StreamPlatformDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = StreamPlatformSerializer
    queryset = StreamPlatform.objects.all()
    lookup_url_kwarg = 'platform_id'
    lookup_field = 'id'
    
    
class WatchListView(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrReadOnly]
    pagination_class   = CPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = WatchListFilter
    
    
    # lookup_field, url_kwarg 그리고 filtering기준이 될 data의 propery가 모두 같아야, 의도한 대로 정상적으로 필터링이 됨
    # lookup_field = 'platform_id'
    # permission_classes = [IsAdminOrReadOnly]
    serializer_class = WatchListSerializer
    queryset = WatchList.objects.all()



class WatchListDetailView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAdminOrReadOnly]
    serializer_class = WatchListSerializer
    queryset = WatchList.objects.all()
    
    def get_object(self):
        queryset = self.get_queryset()
        print(self.kwargs)
        filter = {
        'platform_id'  : self.kwargs['platform_id'],
        'id' :self.kwargs['watchlist_id'],
        }

        obj = get_object_or_404(queryset,**filter)
        return obj