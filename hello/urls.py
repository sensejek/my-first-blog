from ast import Delete
from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post/<int:pk>/delete/', views.DeletePost.as_view(), name='delete_post'),
    path('post/<int:pk>/edit_post/', views.UpdatePost.as_view(), name='edit_post'),
    path('post/new_post/', views.NewPost.as_view(), name='new_post'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
]