from django.urls import path
from .views import *


urlpatterns = [
    path('', ArticleList.as_view(), name='article_list'),
    path('<int:pk>/', ArticleSingle.as_view(), name='article_single'),
]