from django.views.generic import ListView, DetailView

from posts.models import Post


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post
