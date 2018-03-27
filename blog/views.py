from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect

from blog.models import Post
from common.views import get_redirected


def blog_view(request):
    posts = Post.objects.filter(published=True).order_by('-date')

    filter_search = request.GET.get('filter_search')
    filter_category = request.GET.get('filter_category')

    if filter_search != '' and filter_search is not None:
        posts = posts.filter(title__icontains=filter_search)

    if filter_category != '' and filter_category is not None:
        posts = posts.filter(category__name__icontains=filter_category)

    paginator = Paginator(posts, 10)

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/home.html', {'posts': posts})


def post_view(request, slug, id):
    post, post_url = get_redirected(Post, {'pk': id}, {'slug': slug})
    if post_url:
        return redirect(post_url)

    return render(request, 'blog/post.html', {'post': post, })
