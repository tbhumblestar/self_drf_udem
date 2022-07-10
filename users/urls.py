from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import registration_view


urlpatterns = [
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('registration', registration_view, name='registration'),
]
