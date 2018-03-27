from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'genres'


class Game(models.Model):
    order = models.IntegerField(default=100)
    name = models.CharField(max_length=50)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)
    short_description = models.TextField(max_length=500)
    link = models.URLField()
    itch_game_name = models.CharField(max_length=100)
    is_free = models.BooleanField(default=True)
    preview_image = models.ImageField(upload_to='games/preview_image/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'games'
