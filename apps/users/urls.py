from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView 

urlpatterns = [
    path('acces_token/', TokenObtainPairView.as_view(), name='acces'),
    path('refresh_token/', TokenRefreshView.as_view(), name='refresh'),
    path('users/', UserListCreateView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailsView.as_view(), name='user-detail'),
    path('transfers/', HistoryTransfers.as_view(), name='transfer-list'),
    path('transfers/<int:pk>/', HistoryTransferView.as_view(), name='transfer-detail'),
]