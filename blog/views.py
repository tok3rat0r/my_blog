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
    def is_stored_post(self, request, post_id):
        stored_posts = request.session.get('stored_posts')
        if stored_posts is not None:
            return post_id in stored_posts
        else:
            return False

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        is_stored = self.is_stored_post(request, post.id)
        return render(request, "blog/post-detail.html", {
            'post': post,
            'post_tags': post.tags.all(),
            'comment_form': CommentForm(),
            'comments': post.comments.all().order_by('-id'),
            'saved_for_later': is_stored,
        })

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        is_stored = self.is_stored_post(request, post.id)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("single-post-page", args=[slug]))

        return render(request, "blog/post-detail.html", {
            'post': post,
            'post_tags': post.tags.all(),
            'comment_form': comment_form,
            'comments': post.comments.all().order_by('-id'),
            'saved_for_later': is_stored,
        })


class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get('stored_posts')
        context = {}

        if stored_posts is None or len(stored_posts) == 0:
            context['posts'] = []
            context['has_posts'] = False
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context['posts'] = posts
            context['has_posts'] = True

        return render(request, 'blog/stored-posts.html', context)

    def post(self, request):
        stored_posts = request.session.get('stored_posts')
        if stored_posts is None:
            stored_posts = []

        post_id = int(request.POST['post_id'])
        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)

        request.session['stored_posts'] = stored_posts
        return HttpResponseRedirect('/')
