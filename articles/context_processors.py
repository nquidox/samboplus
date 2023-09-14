from articles.models import Article


def summary_list(request):
    sum_list = Article.objects.filter(is_published=True)
    return {'summary_list': sum_list}