from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.start_page, name='start-page'),
    path('posts', views.posts, name='posts-page'),
    path('posts/<slug:slug>', views.single_post, name='single-post-page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
