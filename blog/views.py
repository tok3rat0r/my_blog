from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from .models import Post
from .forms import CommentForm

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


class SinglePostView(View):

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        return render(request, "blog/post-detail.html", {
            'post': post,
            'post_tags': post.tags.all(),
            'comment_form': CommentForm(),
        })

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("single-post-page", args=[slug]))

        return render(request, "blog/post-detail.html", {
            'post': post,
            'post_tags': post.tags.all(),
            'comment_form': comment_form,
        })

