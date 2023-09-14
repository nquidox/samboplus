import datetime

from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic


from .forms import UserLoginForm, CustomUserChangeForm


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home_news')
    else:
        form = UserLoginForm()
    return render(request, 'lk/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home_news')


class CustomUserForm(LoginRequiredMixin, generic.UpdateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    form_class = CustomUserChangeForm
    template_name = 'lk/lk.html'
    success_url = reverse_lazy('lk')
    context_object_name = 'user_profile'

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, *args, **kwargs):
        context = super(CustomUserForm, self).get_context_data(*args, **kwargs)
        context['today'] = datetime.date.today()
        context['page_title'] = 'Личный кабинет'
        return context

    def get_form(self, form_class=None):
        form = super(CustomUserForm, self).get_form(form_class)
        form.fields["agreement_expiration_date"].disabled = True
        form.fields["insurance_expiration_date"].disabled = True
        form.fields["medical_report_expiration_date"].disabled = True
        form.fields["school_certificate_expiration_date"].disabled = True
        return form
