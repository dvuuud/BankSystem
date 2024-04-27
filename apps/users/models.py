from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.crypto import get_random_string
from django.core.validators import RegexValidator 

phone_regex = RegexValidator(regex=r'^\+996\d{9}$', message="Номер телефона необходимо ввести в формате: '+996xxxxxxxxx'.")

class User(AbstractUser):
    phone_number = models.CharField(validators=[phone_regex], max_length=15, verbose_name='Номер телефона')
    age = models.IntegerField(default=0, verbose_name='Возраст')
    wallet_address = models.CharField(max_length=12, unique=True,blank=True ,verbose_name='ID кошелька')
    
    def __str__(self):
        return f'Пользователи'
    
    class Meta:
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'
    
class HistoryTransfer(models.Model):
    from_user = models.ForeignKey(User, related_name='transfers_sent', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='transfers_received', on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False, verbose_name='Сделано')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан в')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма')

    def __str__(self):
        return f'Переводы'
    class Meta:
        verbose_name = 'Перевод'
        verbose_name_plural = 'Переводы'
    