from django.contrib import admin

from assets.models import Category, Asset


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ('order', 'name', 'category', 'link', 'is_free', )
    list_display_links = ('name', )
    list_editable = ('order', )
    ordering = ('order', 'name', )

