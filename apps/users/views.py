from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import *
from rest_framework.views import APIView
from .serializers import *

# Create your views here.
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.request.method == "POST":
            return UserRegisterSerializer
        return UserSerializer

class UserDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
class HistoryTransfers(generics.ListAPIView):
    queryset = HistoryTransfer.objects.all()
    serializer_class = HistoryTransferSerializer
    permission_classes = [IsAuthenticated]
    
class HistoryTransferView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HistoryTransfer.objects.all()
    serializer_class = HistoryTransferSerializer
    permission_classes = [IsAuthenticated]