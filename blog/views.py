from django.shortcuts import render
from datetime import date

all_posts = [
    {
        'slug': "climbing",
        'image': "IMG_20170429_112127.jpg",
        'author': "Owen",
        'date': date(2021, 12, 4),
        'title': "Climbing",
        'excerpt': "This is some text for a blog post about climbing",
        'content': """
           This is some text for a blog post about climbing. I like climbing, it is cool.
           Writing is one of my strong suits. I write words about climbing here.
        """
    },
    {
        'slug': "meow",
        'image': "IMG_20171019_064436.jpg",
        'author': "Dandy",
        'date': date(2017, 8, 15),
        'title': "Meow",
        'excerpt': "Meow meow meow meow meow",
        'content': """
           Meow meow meow meow meow, meow meow. Meow meow meow.
           Meow meow meow meow, meow meow meow meow meow; meow meow!
        """
    },
    {
        'slug': "photography",
        'image': "IMG_20211012_073504.jpg",
        'author': "Cécile",
        'date': date(2021, 10, 19),
        'title': "Photography",
        'excerpt': "I took some photos in Slovenia",
        'content': """
           I took some photos in Slovenia. Look how cool they are! We went to some pretty places
           and I took many, many photos.
        """
    }
]

def get_date(post):
    return post['date']

# Create your views here.


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
    post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blog/post-detail.html', {'post': post})
