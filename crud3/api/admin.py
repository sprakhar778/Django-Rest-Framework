from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'created_at', 'updated_at')
    search_fields = ('title', 'author')
    list_filter = ('created_at', 'author')
    ordering = ('-created_at',)
admin.site.register(Blog)