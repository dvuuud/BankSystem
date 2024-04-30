from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import AllowAny, IsAuthenticated
# My imports
from .models import User, HistoryTransfer
from .permissions import UserPermissions
from .serializers import UserSerializer, HistoryTransferSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

class UserAPiViewSet(GenericViewSet, 
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication] 
        
    def get_permissions(self):
        if self.action in ('DELETE', 'PUT ','PATCH'):
            return (UserPermissions(),)
        return (AllowAny(),)
    
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class HistoryTransferViewSet(GenericViewSet,
                             mixins.ListModelMixin,
                             mixins.CreateModelMixin,
                             mixins.DestroyModelMixin,
                             mixins.UpdateModelMixin,
                             mixins.RetrieveModelMixin):
    queryset = HistoryTransfer.objects.all()
    serializer_class = HistoryTransferSerializer
    authentication_classes = [JWTAuthentication] 
    