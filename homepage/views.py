from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Mario',
        'title': 'Blog post 1',
        'content': 'First content',
        'date_posted': 'July 12, 2019',
    },
    {
        'author': 'Marija',
        'title': 'Blog post 2',
        'content': 'Second content',
        'date_posted': 'July 13, 2019',
    }
]


# Create your views here.
def home(request):
    return render(request, 'homepage/home.html')


def about(request):
    return render(request, 'homepage/about.html', {'title': 'About'})


def blog(request):
    context = {
        'posts': posts
    }
    return render(request, 'homepage/blog.html', context)  # Kroz context šalješ na frontu varijable


def projects(request):
    return render(request, 'homepage/projects.html')
