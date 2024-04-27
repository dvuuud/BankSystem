from rest_framework import serializers
from .models import User, HistoryTransfer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'age', 'wallet_address']
        # Register
class UserRegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=255, write_only=True, label='Подтверждения пароля')
    class Meta:
        model = User 
        fields = ['id','email','password', 'confirm_password']
        
    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'password':'Пароли отличаются'})
        return attrs 
    
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['email'] 
            
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class HistoryTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryTransfer
        fields = ['id', 'from_user', 'to_user', 'is_completed', 'created_at', 'amount']
