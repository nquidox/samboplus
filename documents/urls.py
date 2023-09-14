from django.urls import path
from .views import *


urlpatterns = [
    path('', DocumentsView.as_view(), name='documents'),
]