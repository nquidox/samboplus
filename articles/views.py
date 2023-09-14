from django.views.generic import ListView, DetailView

from .models import Article


class ArticleList(ListView):
    model = Article
    template_name = 'articles/articles_list.html'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Статьи'
        context['button_name'] = 'Читать полностью'
        return context

    def get_queryset(self):
        return Article.objects.filter(is_published=True)


class ArticleSingle(DetailView):
    model = Article
    template_name = 'articles/article_single.html'
    context_object_name = 'article_single'
    # pk_url_kwarg = 'single_id'
