from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from django.http import HttpResponse


class PostListView(ListView):
    model = Post
    # PostListView trazi template_name u ovom formatu
    # <app>/<model>_<viewtype>.html
    # homepage/post_list.html
    template_name = 'homepage/blog.html'
    context_object_name = 'posts'
    # Promjena redosljeda postova
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


# Create your views here.
def home(request):
    return render(request, 'homepage/home.html')


def about(request):
    return render(request, 'homepage/about.html', {'title': 'About'})


def blog(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'homepage/blog.html', context)  # Kroz context šalješ na frontu varijable


def projects(request):
    return render(request, 'homepage/projects.html')
