from django.urls import path
from .views import PostListView, PostDetailView
from . import views

urlpatterns = [
    path('', views.home, name='homepage-home'),
    path('about/', views.about, name='homepage-about'),
    path('blog/', PostListView.as_view(), name='homepage-blog'),
    # int:pk ogranicavam na integer, u slucaju da dodje string
    path('blog/post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('projects/', views.projects, name='homepage-projects'),
]
