from django.contrib import admin

# Register your models here.

from .models import InfoBlock


class InfoBlockAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'side', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('title',)
    list_editable = ('is_published',)


admin.site.register(InfoBlock, InfoBlockAdmin)
