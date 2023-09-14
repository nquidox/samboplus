from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from .models import About


class AboutView(TemplateView):
    model = About
    template_name = 'about/about.html'
    contex_object_name = 'about'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'О нас'
        context['about'] = About.objects.get(pk=1)
        context['contacts'] = About.objects.get(pk=2)
        return context
