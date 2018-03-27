from django.conf.urls import url

from blog import views


urlpatterns = [
    url(r'^$', views.blog_view, name='blog'),
    url(r'^(?P<slug>[-\w\d]+)-(?P<id>\d+)/$', view=views.post_view, name='post'),
]
