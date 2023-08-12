from django.db import models
from django.contrib.auth.models import User


class Feedback(models.Model):
    name = models.CharField('Имя', max_length=50)
    email = models.EmailField('Email', max_length=120, blank=True, null=True)
    phone = models.CharField('Номер телефона', max_length=15)
    message = models.TextField('Сообщение', max_length=120, blank=True, null=True)
    # time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')
    # user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'
        # ordering = ['-time_create']
        # db_table = 'app_feedback'

    def __str__(self):
        return self.name

