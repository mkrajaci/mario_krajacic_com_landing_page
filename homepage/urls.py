from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views

urlpatterns = [
    path('', views.home, name='homepage-home'),
    path('about/', views.about, name='homepage-about'),
    path('blog/', PostListView.as_view(), name='homepage-blog'),
    path('blog/user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    # int:pk ogranicavam na integer, u slucaju da dodje string
    path('blog/post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('blog/post/new/', PostCreateView.as_view(), name='post-create'),
    path('blog/post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('blog/post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('projects/', views.projects, name='homepage-projects'),
]
