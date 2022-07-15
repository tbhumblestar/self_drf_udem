from django.shortcuts import get_object_or_404
from rest_framework.filters import OrderingFilter
# Create your views here.
from rest_framework import generics
from objects_apps.models import *
from objects_apps.serializers import (
                                    StreamPlatformSerializer,
                                    WatchListSerializer,
                                    ReviewSerializer
                                    )
from rest_framework.permissions import (IsAuthenticated,IsAuthenticatedOrReadOnly)

from rest_framework.exceptions import ValidationError
from django_filters import rest_framework as filters

from objects_apps.permissions import IsAdminOrReadOnly,ReviewUserOrReadOnly
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
    pagination_class   = WatchListPagination
    serializer_class = WatchListSerializer
    queryset = WatchList.objects.all()
    
    filter_backends = [filters.DjangoFilterBackend,OrderingFilter]
    filterset_class = WatchListFilter
    ordering_fields =['platform_id']
    
    # lookup_field, url_kwarg 그리고 filtering기준이 될 data의 propery가 모두 같아야, 의도한 대로 정상적으로 필터링이 됨
    # lookup_field = 'platform_id'
    # permission_classes = [IsAdminOrReadOnly]
    



class WatchListDetailView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAdminOrReadOnly]
    serializer_class = WatchListSerializer
    queryset = WatchList.objects.all()
    
    def get_object(self):
        queryset = self.get_queryset()

        filter = {
        'platform_id'  : self.kwargs['platform_id'],
        'id' :self.kwargs['watchlist_id'],
        }

        obj = get_object_or_404(queryset,**filter)
        return obj
    
class ReviewLCView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    # permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        watchlist_id = self.kwargs['watchlist_id']
        return Review.objects.filter(watchlist_id=watchlist_id)

    
    def perform_create(self,serializer):
        watchlist_id = self.kwargs.get('watchlist_id')
        watchlist = WatchList.objects.get(id=watchlist_id)
        review_user = self.request.user
        
        # if Review.objects.filter(watchlist=watchlist,review_user=review_user).exist():
        #     raise ValidationError("You have already reviewd the watchlist")
        # else:
        serializer.save(watchlist_id=watchlist_id,review_user_id=3)



class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    # permission_classes = (ReviewUserOrReadOnly,)

    def get_object(self):
        queryset = self.get_queryset()
        review_id = self.kwargs['review_id']
        obj = get_object_or_404(queryset,id=review_id)
        self.check_object_permissions(self.request, obj)
        return obj
        

class UserReviewListView(generics.ListAPIView):
    serializer_class = ReviewSerializer
    def get_queryset(self):
        username = self.request.query_params.get('username',None)
        
        return Review.objects.filter(review_user__username=username)