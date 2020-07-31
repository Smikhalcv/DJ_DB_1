from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(verbose_name='Модель', max_length=200)
    price = models.FloatField(verbose_name='Цена', blank=True)
    image = models.ImageField(verbose_name='Изображение', upload_to='media', blank=True)
    release_date = models.DateField(verbose_name='Дата выхода', blank=True)
    lte_exists = models.BooleanField(verbose_name='lte', blank=True)
    slug = models.SlugField(blank=True)
