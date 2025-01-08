import hashlib
from rest_framework import serializers
from django.utils.crypto import get_random_string
from .models import User, HistoryTransfer
# my serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'phone_number', 'age', 'password', 'created_at', 'confirm_password', 'balance', 'wallet_address')
        
    def validate(self, attrs):
        if len(attrs['password']) < 8:
            raise serializers.ValidationError('Пароль слишком короткий')
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError("Пароли отличаются")
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        password = validated_data.pop('password')
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        validated_data['password'] = hashed_password
        return super().create(validated_data)

    def update(self, instance, validated_data):     
        validated_data.pop('confirm_password')
        if 'password' in validated_data:
            password = validated_data.pop('password')
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            validated_data['password'] = hashed_password
        return super().update(instance, validated_data)

class HistoryTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryTransfer
        fields = ('id', 'from_user', 'to_user', 'is_completed','amount')
