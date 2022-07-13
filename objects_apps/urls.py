
from django.urls import path, include
from .views import StreamPlatformView,StreamPlatformDetailView,WatchListView,WatchListDetailView

urlpatterns = [
    path('stream',StreamPlatformView.as_view(),name='StreamPlatformView' ),
    path('stream/<int:platform_id>',StreamPlatformDetailView.as_view(),name='StreamPlatformDetailView' ),
    path('stream/<int:platform_id>/watchlist',WatchListView.as_view(),name='WatchListView' ),
    path('stream/<int:platform_id>/watchlist/<int:watchlist_id>',WatchListDetailView.as_view(),name='WatchListDetailView' ),
]
