from django.views.generic import ListView, DetailView

from .models import Post


class HomePageView(ListView):
    model = Post
    template_name = "home.html"


class PostDetailView(DetailView):
    model = Post
    template_name = "detail.html"
