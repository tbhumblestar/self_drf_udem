
from django.urls import path, include
from .views import StreamPlatformView,StreamPlatformDetailView,WatchListView,WatchListDetailView,UserReviewListView,ReviewDetailView,ReviewLCView

urlpatterns = [
    path('stream',StreamPlatformView.as_view(),name='StreamPlatformView' ),
    path('stream/<int:platform_id>',StreamPlatformDetailView.as_view(),name='StreamPlatformDetailView' ),
    path('stream/<int:platform_id>/watchlist',WatchListView.as_view(),name='WatchListView' ),
    path('stream/<int:platform_id>/watchlist/<int:watchlist_id>',WatchListDetailView.as_view(),name='WatchListDetailView' ),
    path('stream/<int:platform_id>/watchlist/<int:watchlist_id>/review',ReviewLCView.as_view(),name='ReviewLCView' ),
    path('stream/<int:platform_id>/watchlist/<int:watchlist_id>/review/<int:review_id>',ReviewDetailView.as_view(),name='ReviewDetailView' ),
    path('review',UserReviewListView.as_view(),name='UserReviewListView' ),
]
