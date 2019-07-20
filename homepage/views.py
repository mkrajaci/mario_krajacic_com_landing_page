from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post


# Pogledaj 10 video tutoriala za objasnjenja ovih class based viewa
# https://youtu.be/-s7e_Fy6NRU
class PostListView(ListView):
    model = Post
    # PostListView trazi template_name u ovom formatu
    # <app>/<model>_<viewtype>.html
    # homepage/post_list.html
    template_name = 'homepage/blog.html'
    context_object_name = 'posts'
    # Promjena redosljeda postova
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'homepage/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    # Presretanje form_valid metode i njena nadogradnja
    # Postavljanje autora posta na trenutno logiranog korisnika
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# Ovi Mixini sluze za provjeru je li korisnik logiran i da ne smije editirati
# postove drugog korisnika
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    # Presretanje form_valid metode i njena nadogradnja
    # Postavljanje autora posta na trenutno logiranog korisnika
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/blog'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


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
