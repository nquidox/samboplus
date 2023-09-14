from django.db import models

# Create your models here.


class InfoBlock(models.Model):
    choose_side = [('left', 'слева'), ('right', 'справа')]

    title = models.CharField(max_length=250, verbose_name='Название блока')
    image = models.ImageField(upload_to='infoblocks/%Y/%m/', blank=True, verbose_name='Изображение')
    text = models.TextField(blank=True, verbose_name='Содержание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Изменено')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    side = models.CharField(max_length=100, blank=False, choices=choose_side, verbose_name='Сторона')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Информационный блок'
        verbose_name_plural = 'Информационные блоки'
        ordering = ['-created_at']
