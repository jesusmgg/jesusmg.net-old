"""jesusmgnet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from jesusmgnet import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

    url(r'^blog/', include('blog.urls'), name='blog'),
    url(r'^games/', include('games.urls'), name='games'),
    url(r'^assets/', include('assets.urls'), name='assets'),

    url(r'^$', views.home_view, name='home'),
    url(r'^contact/', views.contact_view, name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Change admin site title
admin.site.site_header = "Jesús González"
admin.site.site_title = "Official Site"
