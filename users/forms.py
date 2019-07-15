from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


'''
    Ovdje nasljedujem originalni model i klasu od forms i nadogradjujem sa svojim custom poljem email.
    Da bi poslije mogao koristiti polje trebam importati ovu klasu u py u kojem koristim
'''


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
