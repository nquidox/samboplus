from django.views.generic import ListView, DetailView


from .models import News


class HomeNews(ListView):
    model = News
    template_name = 'news/news.html'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Новости'
        context['button_name'] = 'Читать полностью'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class HomeNewsSingle(DetailView):
    model = News
    template_name = 'news/single.html'
    context_object_name = 'single'
    # pk_url_kwarg = 'single_id'
