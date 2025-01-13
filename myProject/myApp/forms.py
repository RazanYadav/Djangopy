from django import forms
from .models import Book
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Book Form
class BookForm(forms.Form):
    bk_name = forms.CharField(label='Book Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    bk_number = forms.IntegerField(label='Book Number', widget=forms.NumberInput(attrs={'class': 'form-control'}))

# Login Form
class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

# Register Form (User Creation)
class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, label='First Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, label='Last Name', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))

# myApp/forms.py
from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter note title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter note content', 'rows': 5}),
        }

from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']  # Fields to display in the form
