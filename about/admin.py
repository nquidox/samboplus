from django.contrib import admin

# Register your models here.

from .models import About


class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('title',)


admin.site.register(About, AboutAdmin)
