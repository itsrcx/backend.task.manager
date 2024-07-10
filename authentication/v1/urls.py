from django.urls import path

from authentication.v1.views import (
    DecoratedTokenObtainPairView, 
    DecoratedTokenRefreshView, 
    DecoratedTokenVerifyView, 
    DecoratedTokenBlacklistView
)

urlpatterns = [
    path(
        'api/token/', 
        DecoratedTokenObtainPairView.as_view(), 
        name='token_obtain_pair'
    ),
    path(
        'api/token/refresh/', 
        DecoratedTokenRefreshView.as_view(), 
        name='token_refresh'
    ),
    path(
        'api/token/verify/', 
        DecoratedTokenVerifyView.as_view(), 
        name='token_verify'
    ),
    path(
        'api/token/blacklist/', 
        DecoratedTokenBlacklistView.as_view(), 
        name='token_blacklist'
    ),
]
