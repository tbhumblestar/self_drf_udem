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


from objects_apps.permissions import IsAdminOrReadOnly

class StreamPlatformView(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = StreamPlatformSerializer
    queryset = StreamPlatform.objects.all()

class StreamPlatformDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = StreamPlatformSerializer
    queryset = StreamPlatform.objects.all()
    
    #url_kwargs를 바꿔주기 위한 대여정.. 이렇게 해주지 않으면 기존 get_object에 의해 lookup_field, url_kwarg 그리고 filtering기준이 될 data의 propery가 모두 같아야만 함
    def get_object(self):
        queryset = self.get_queryset()
        platfomr_id = self.kwargs['platform_id']
        obj = get_object_or_404(queryset,id=platfomr_id)
        return obj
    
    
class WatchListView(generics.ListCreateAPIView):
    
    # lookup_field, url_kwarg 그리고 filtering기준이 될 data의 propery가 모두 같아야, 의도한 대로 정상적으로 필터링이 됨
    lookup_field = 'platform_id'
    
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