from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage-home'),
    path('about/', views.about, name='homepage-about'),
    path('blog/', views.blog, name='homepage-blog'),
    path('projects/', views.projects, name='homepage-projects'),
]
