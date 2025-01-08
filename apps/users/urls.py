from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView 
from django.urls import path

from .views import UserAPiViewSet, HistoryTransferViewSet
# my urls
router = DefaultRouter()
router.register('users', UserAPiViewSet, basename='api_user')
router.register('history_transfers', HistoryTransferViewSet, basename='api_history_transfers')

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh')
]

urlpatterns += router.urls
