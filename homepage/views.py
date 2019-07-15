from django.shortcuts import render
from .models import Post
from django.http import HttpResponse


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
