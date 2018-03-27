from django.shortcuts import render

from games.models import Game


def games_view(request):
    games = Game.objects.all().order_by('order')
    return render(request, 'games/games.html', {'games': games, })
