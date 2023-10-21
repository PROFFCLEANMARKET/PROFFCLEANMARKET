from django.db import models


class Category(models.Model):
  name = models.CharField(max_length=100, verbose_name='Название')

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = 'Категория товара'
    verbose_name_plural = 'Категории товара'
