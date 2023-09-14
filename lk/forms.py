from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper

from lk.models import CustomUser


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-label'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-label'}))


# форма для создания, проверить нужны ли все эти поля
class CustomUserCreateForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'patronymic', 'last_name', 'birth_date', 'gender', 'place_of_birth', 'home_address',
                  'current_weight', 'current_height', 'chest', 'waist', 'hips', 'foot',
                  'fullname1', 'phone_number1', 'fullname2', 'phone_number2', 'email')

    def clean_current_weight(self):
        current_weight = self.cleaned_data['current_weight']
        if current_weight < 0:
            raise ValidationError('Вес должен быть положительным числом')
        return current_weight


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'patronymic', 'last_name', 'birth_date', 'gender', 'place_of_birth', 'home_address',
                  'current_weight', 'current_height', 'chest', 'waist', 'hips', 'foot',
                  'fullname1', 'phone_number1', 'fullname2',
                  'phone_number2', 'email', 'photo',
                  'agreement', 'agreement_expiration_date',
                  'application_blank',
                  'passport',
                  'insurance', 'insurance_expiration_date',
                  'medical_report', 'medical_report_expiration_date',
                  'school_certificate', 'school_certificate_expiration_date')

    def clean_current_weight(self):
        current_weight = self.cleaned_data['current_weight']
        if current_weight < 0:
            raise ValidationError('Вес должен быть положительным числом')
        return current_weight

    def clean_foot(self):
        foot = self.cleaned_data['foot']
        if foot <0:
            raise ValidationError('Размер стопы должен быть положительным числом')
        return foot

    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        # снимаем автоназвания полей
        self.fields['first_name'].label = False
        self.fields['patronymic'].label = False
        self.fields['last_name'].label = False
        self.fields['birth_date'].label = False
        self.fields['gender'].label = False
        self.fields['place_of_birth'].label = False
        self.fields['home_address'].label = False
        self.fields['current_weight'].label = False
        self.fields['current_height'].label = False
        self.fields['chest'].label = False
        self.fields['waist'].label = False
        self.fields['hips'].label = False
        self.fields['foot'].label = False
        self.fields['fullname1'].label = False
        self.fields['phone_number1'].label = False
        self.fields['fullname2'].label = False
        self.fields['phone_number2'].label = False
        #
        self.fields['photo'].label = False
        self.fields['photo'].widget = forms.FileInput(attrs={})
        self.fields['email'].label = False
        #
        self.fields['application_blank'].label = False
        self.fields['application_blank'].widget = forms.FileInput(attrs={})
        #
        self.fields['passport'].label = False
        self.fields['passport'].widget = forms.FileInput(attrs={})
        #
        self.fields['agreement'].label = False
        self.fields['agreement'].widget = forms.FileInput(attrs={})
        #
        self.fields['insurance'].label = False
        self.fields['insurance'].widget = forms.FileInput(attrs={})
        #
        self.fields['medical_report'].label = False
        self.fields['medical_report'].widget = forms.FileInput(attrs={})
        #
        self.fields['school_certificate'].label = False
        self.fields['school_certificate'].widget = forms.FileInput(attrs={})


class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = CustomUser
        fields = ('old_password', 'new_password1', 'new_password2')
