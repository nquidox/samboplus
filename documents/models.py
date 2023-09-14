from django.db import models
import os
import datetime

# Create your models here.


def documents_path(instance, filename):
    fn = os.path.splitext(filename)[0]
    ext = os.path.splitext(filename)[1]
    date = datetime.date.strftime(datetime.date.today(), '-%d-%B-%Y')
    new_fn = fn+date+ext
    return 'documents/federation_documents/{0}'.format(new_fn)


class Document(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Содержание')
    file = models.FileField(upload_to=documents_path, blank=True, null=True, verbose_name='Файл')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'

