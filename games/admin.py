from django.contrib import admin

from games.models import Genre, Game


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('order', 'name', 'genre', 'link', 'is_free', )
    list_display_links = ('name', )
    list_editable = ('order', )
    ordering = ('order', 'name', )
