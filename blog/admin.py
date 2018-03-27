from django.contrib import admin

from blog.models import Category, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('date', 'category', 'title', 'published', )
    list_display_links = ('title', )
    ordering = ('date', 'category',  'title', )
