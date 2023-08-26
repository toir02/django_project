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
    change_date = models.DateField(verbose_name='дата изменения', **NULLABLE)

    def __str__(self):
        return f'{self.product_name}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('product_name',)


class Category(models.Model):
    category_name = models.CharField(max_length=50, verbose_name='наименование')
    category_description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('category_name',)


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    description = models.TextField(verbose_name='содержимое')
    image = models.ImageField(upload_to='blog/', verbose_name='изображение', **NULLABLE)
    create_date = models.DateField(verbose_name='дата создания')
    sign_publication = models.CharField(max_length=100, verbose_name='признак публикации')
    count_views = models.IntegerField(verbose_name='количество просмотров')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
