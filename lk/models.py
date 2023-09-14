import random
import os
import string
import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


def user_directory_path(instance, filename):
    fn = os.path.splitext(filename)[0]
    ext = os.path.splitext(filename)[1]
    rand = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(8))
    date = datetime.date.strftime(datetime.date.today(), '-%d-%B-%Y-')
    new_fn = fn+date+rand+ext
    return 'documents/{0}/{1}'.format(instance.username, new_fn)


def photo_upload(instance, filename):
    return 'documents/{0}/{1}'.format(instance.username, filename)


class CustomUser(AbstractUser, PermissionsMixin):
    # список полов на выбор
    genders = [('male', 'мужской'), ('female', 'женский')]

    # фото
    photo = models.ImageField(upload_to=photo_upload, max_length=200, blank=True, verbose_name='Фотография')

    email = models.EmailField(max_length=200, blank=True, verbose_name='Адрес электронной почты')

    # информация о спортсмене
    patronymic = models.CharField(max_length=200, blank=True, verbose_name='Отчество')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    gender = models.CharField(max_length=20, blank=True, choices=genders, verbose_name='Пол')
    place_of_birth = models.CharField(max_length=200, blank=True, verbose_name='Место рождения')
    home_address = models.CharField(max_length=200, blank=True, verbose_name='Домашний адрес')
    current_weight = models.FloatField(default=0, blank=False, verbose_name='Текущий вес')
    current_height = models.PositiveIntegerField(default=0, blank=False, verbose_name='Текущий рост')
    chest = models.PositiveIntegerField(default=0, blank=False, verbose_name='Обхват груди')
    waist = models.PositiveIntegerField(default=0, blank=False, verbose_name='Размер талии')
    hips = models.PositiveIntegerField(default=0, blank=False, verbose_name='Размер бедер')
    foot = models.FloatField(default=0, blank=False, verbose_name='Размер стопы')


    # информация о родителях/опекунах
    fullname1 = models.CharField(max_length=200, blank=True, verbose_name='Ф.И.О.')
    fullname2 = models.CharField(max_length=200, blank=True, verbose_name='Ф.И.О.')
    phone_number1 = PhoneNumberField(max_length=12, null=True, blank=True, verbose_name='Телефон')
    phone_number2 = PhoneNumberField(max_length=12, null=True, blank=True, verbose_name='Телефон')

    # документы
    application_blank = models.FileField(upload_to=user_directory_path, blank=True, null=True, verbose_name='Заявление')
    #
    passport = models.FileField(upload_to=user_directory_path, blank=True, null=True,
                                verbose_name='Свидетельство о рождении/паспорт')
    #
    agreement = models.FileField(upload_to=user_directory_path, blank=True, null=True, verbose_name='Договор')
    agreement_expiration_date = models.DateField(blank=True, null=True, verbose_name='Дата истечения договора')
    #
    insurance = models.FileField(upload_to=user_directory_path, blank=True, null=True, verbose_name='Страховка')
    insurance_expiration_date = models.DateField(blank=True, null=True, verbose_name='Дата истечения страховки')
    #
    medical_report = models.FileField(upload_to=user_directory_path, blank=True, null=True,
                                      verbose_name='Медицинское заключение')
    medical_report_expiration_date = models.DateField(blank=True, null=True,
                                                      verbose_name='Дата истечения медицинского заключения')
    #
    school_certificate = models.FileField(upload_to=user_directory_path, blank=True, null=True,
                                          verbose_name='Справка из школы')
    school_certificate_expiration_date = models.DateField(blank=True, null=True,
                                                          verbose_name='Дата истечения справки из школы')

    debt = models.BooleanField(default=False, verbose_name='Задолженность')


