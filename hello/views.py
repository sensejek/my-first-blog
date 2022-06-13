from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post, Comment
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from .forms import CommentForm


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs["pk"]

        form = CommentForm()
        post = get_object_or_404(Post, pk=pk)
        comments = post.comments.all()

        context['post'] = post
        context['comments'] = comments
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)

        post = Post.objects.filter(id=self.kwargs['pk'])[0]
        comments = post.comments.all()

        context['post'] = post
        context['comments'] = comments
        context['form'] = form

        if form.is_valid():

            body = form.cleaned_data['body']

            comment = Comment.objects.create(author=request.user, body=body, post=post)

            form = CommentForm()
            context['form'] = form
            return self.render_to_response(context=context)

        return self.render_to_response(context=context)

class NewPost(PermissionRequiredMixin, generic.CreateView):
    model = Post
    template_name = 'new_post.html'
    fields = ['title', 'content', 'status']
    permission_required = "hello.add_post"

class UpdatePost(PermissionRequiredMixin, generic.UpdateView):
    model = Post
    template_name = 'edit_post.html'
    fields = ['title', 'content']
    permission_required = "hello.change_post"

class DeletePost(PermissionRequiredMixin, generic.DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    permission_required = "hello.delete_post"

