from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from .models import Document


class DocumentsView(ListView):
    model = Document
    template_name = 'documents/documents.html'
    context_object_name = 'document_context'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Документы'
        return context

0