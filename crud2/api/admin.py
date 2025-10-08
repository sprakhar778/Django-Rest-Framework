from django.contrib import admin
from .models import Blog
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'author')
    list_filter = ('created_at',)
    ordering = ('-created_at',)


admin.site.register(Blog, BlogAdmin)