from django.conf.urls import url

from assets import views


urlpatterns = [
    url(r'^$', views.assets_view, name='assets'),
]