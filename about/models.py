from django.db import models

# Create your models here.


class About(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Содержание')

    class Meta:
        verbose_name = 'Информация о клубе'
        verbose_name_plural = 'Информация о клубе'

    def __str__(self):
        return self.title
