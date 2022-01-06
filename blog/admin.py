from django.contrib import admin
from .models import Author, Tag, Post, Comment

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'author']
    list_filter = ['author', 'tags', 'date']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'user_email', 'post']


admin.site.register(Comment, CommentAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
