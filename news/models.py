from django.db import models
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image
import os
import io

# Create your models here.
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Содержание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Изменено')
    image = models.ImageField(upload_to='photos/%Y/%m/', max_length=200, blank=True, verbose_name='Изображение')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    announcement = models.CharField(max_length=150, blank=True, verbose_name='Краткое объявление')

    def get_absolute_url(self):
        return reverse('single_news', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']
