from news.models import News


def announcements(request):
    # anno_list = News.objects.all()
    anno_list = News.objects.filter(is_published=True)
    return {'anno_list': anno_list}
