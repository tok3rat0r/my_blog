from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.StartPageView.as_view(), name='start-page'),
    path('posts', views.PostsView.as_view(), name='posts-page'),
    path('posts/<slug:slug>', views.SinglePostView.as_view(), name='single-post-page'),
    path('read-later', views.ReadLaterView.as_view(), name='read-later'),
]
