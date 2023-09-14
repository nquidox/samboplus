from django.urls import path, reverse_lazy
from .views import *

from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, PasswordResetView, \
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('', CustomUserForm.as_view(), name='lk'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),

    # in-site password change
    path('change_password/',
         PasswordChangeView.as_view(template_name='lk/change_password.html',
                                    success_url=reverse_lazy('password_change_done')),
         name='change_password'),

    path('change_password/done/',
         PasswordChangeDoneView.as_view(template_name='lk/change_password_done.html'),
         name='password_change_done'),

    # e-mail password change
    path('reset_password', PasswordResetView.as_view(template_name='lk/reset_password.html'),
         name='reset_password'),

    path('password_reset_done', PasswordResetDoneView.as_view(template_name='lk/password_reset_done.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='lk/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('new_password', PasswordResetCompleteView.as_view(template_name='lk/password_reset_complete.html'),
         name='password_reset_complete'),

]
