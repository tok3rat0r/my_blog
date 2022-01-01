from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView
from .models import Post

# Create your views here.
all_posts = Post.objects.all()


def get_date(post):
    return post.date


class StartPageView(TemplateView):
    template_name = "blog/index.html"
    sorted_posts = sorted(all_posts, key=get_date, reverse=True)
    latest_posts = sorted_posts[-3:]
    extra_context = {'latest_posts': latest_posts}


class PostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = 'all_posts'


class SinglePostView(DetailView):
    template_name = "blog/post-detail.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = self.object.tags.all()
        return context
