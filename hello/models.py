from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


STATUS = (
    (0,"Wersja robocza"),
    (1,"Opublikowane")
)

class Post(models.Model):
    title = models.CharField(verbose_name = "Tytuł", max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'blog_posts', verbose_name = "Autor", default = '1')
    content = models.TextField(verbose_name = "Treść")
    created_on = models.DateTimeField(verbose_name = "Utworzono", auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.pk)])

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name='comments', verbose_name = "Autor")
    body = models.TextField(verbose_name = "Treść")
    created_on = models.DateTimeField(verbose_name = "Utworzono", auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.author)
