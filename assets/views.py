from django.shortcuts import render

from assets.models import Asset


def assets_view(request):
    assets = Asset.objects.all()
    return render(request, 'assets/assets.html', {'assets': assets, })
