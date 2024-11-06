from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class mortgage_list(models.Model):

    STATUS_LIST = [
        (True, 'active'),
        (False, 'deleted')
    ]

    title = models.CharField(verbose_name='Название', max_length=30)
    description = models.CharField(verbose_name='Описание', max_length=255)
    desc_extended = models.TextField(verbose_name='Расширенное описание', blank=True)
    image = models.URLField(verbose_name='Изображение', null=True, blank=True)
    status = models.BooleanField(choices=STATUS_LIST, default='active', verbose_name='Статус')

    class Meta:
        db_table = 'mortgage'
        verbose_name = 'mortgage'
        verbose_name_plural = 'mortgages'

class calculation(models.Model):

    STATUS_LIST=[
        (1, 'draft'),
        (0, 'deleted'), 
        (2, 'formed'), 
        (3, 'completed'), 
        (4, 'rejected')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    value = models.IntegerField(verbose_name='Сумма', default=1000000)
    date_creation = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    status = models.IntegerField(choices=STATUS_LIST, default=1, verbose_name='Статус')

    class Meta:
        db_table = 'calculation'
        verbose_name = 'calculation'
        verbose_name_plural = 'calculations'
 
class calculation_content(models.Model):

    calculation = models.ForeignKey(calculation, on_delete=models.CASCADE)
    mortgage_type = models.ForeignKey(mortgage_list, on_delete=models.CASCADE)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2, default=5.00)

    class Meta:
        db_table = 'calculation_content'
        verbose_name = 'calculation_content'
        verbose_name_plural = 'calculation_content'
        
        unique_together = ('calculation', 'mortgage_type') #запрещаем добавлять 2 одинаковые услуги
