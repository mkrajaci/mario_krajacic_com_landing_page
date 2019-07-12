from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def blog_home(request):
    return HttpResponse('<h1>Blog home</h1>')


def blog_about(request):
    return HttpResponse('<h1>Blog about</h1>')
