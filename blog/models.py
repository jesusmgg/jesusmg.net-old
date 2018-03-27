from django.contrib.auth.models import User
from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField
from django.template import defaultfilters
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'


class Post(models.Model):
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, blank=True)
    author = models.ForeignKey(User)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    preview_image = models.ImageField(upload_to='blog/preview_image/', blank=True, null=True)
    content = RichTextUploadingField()
    published = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug, 'id': self.id})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'posts'
