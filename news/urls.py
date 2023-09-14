from django.urls import path
from .views import *


urlpatterns = [
    path('', HomeNews.as_view(), name='home_news'),
    path('single/<int:pk>/', HomeNewsSingle.as_view(), name='single_news'),
]