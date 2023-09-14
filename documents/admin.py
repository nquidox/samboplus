from django.contrib import admin

# Register your models here.

from .models import Document


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('title',)


admin.site.register(Document, DocumentAdmin)