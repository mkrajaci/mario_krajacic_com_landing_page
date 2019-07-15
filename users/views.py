from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.


def register(request):
    if request.method == 'POST':
        # Dohvacanje podataka s forme za registraciju
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            '''
            Moguce poruke:
            messages.debug
            messages.info
            messages.success
            messages.warning
            messages.error
            '''
            messages.success(request, f'Account created for {username}!')
            return redirect('homepage-blog')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
