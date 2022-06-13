from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post','body', 'created_on')
    list_filter = ("created_on",)
    search_fields = ['author', 'body']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)