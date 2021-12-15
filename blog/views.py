from django.shortcuts import render
from .models import Post

# Create your views here.
all_posts = Post.objects.all()


def get_date(post):
    return post.date


def start_page(request):
    sorted_posts = sorted(all_posts, key=get_date, reverse=True)
    latest_posts = sorted_posts[-3:]
    return render(request, 'blog/index.html', {
        'posts': latest_posts,
    })


def posts(request):
    sorted_posts = sorted(all_posts, key=get_date, reverse=True)
    return render(request, 'blog/all-posts.html', {
        'all_posts': sorted_posts,
    })


def single_post(request, slug):
    post = next(post for post in all_posts if post.slug == slug)
    return render(request, 'blog/post-detail.html', {'post': post, 'tags': post.tags.all()})
