from django.db import models

class Client(models.Model):
    name = models.CharField(verbose_name='ФИО', max_length=200)
    email = models.EmailField(verbose_name='E-mail', max_length=200)
    phone = models.CharField(verbose_name='Номер телефона', max_length=200)
    address = models.TextField(verbose_name='Адрес')
    answer = models.TextField(verbose_name='Ответ', choices=[('yes', 'Да'), ('no', 'Нет')], default='no')

    def __str__(self):
        return f'{self.name} {self.email} {self.phone} {self.address} {self.answer}'
    
    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ['name']