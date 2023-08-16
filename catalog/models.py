from django.db import models

NULLABLE = {'blank': True,
            'null': True}


class Product(models.Model):
    product_name = models.CharField(max_length=50, verbose_name='наименование')
    product_description = models.TextField(verbose_name='описание')
    product_image = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)
    product_category = models.CharField(max_length=30, verbose_name='категория')
    product_price = models.IntegerField(verbose_name='цена')
    create_date = models.DateField(verbose_name='дата создания')
    change_date = models.DateField(verbose_name='дата изменения')

    def __str__(self):
        return (f'{self.product_name} {self.product_description} {self.product_image} {self.product_category} '
                f'{self.product_price} {self.create_date} {self.change_date}')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('product_name',)
