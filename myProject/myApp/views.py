from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Book
# myApp/views.py
from .forms import NoteForm  # Ensure this is the correct import


# LoginForm class
class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

# View for logging in
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home after login
            else:
                form.add_error(None, 'Invalid credentials')  # Add error message to form
    else:
        form = LoginForm()
    return render(request, 'myApp/login.html', {'form': form})

# View for logging out
def logout_view(request):
    logout(request)  # Logs out the user
    return redirect('login')  # Redirect to the login page after logout

# Home page view
def home(request):
    books = Book.objects.all()  # Get all books from the database
    return render(request, 'myApp/home.html', {'books': books})  # Pass the books to the template

# BookForm for adding and updating books
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

# View to add a book
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new book to the database
            return redirect('add_book')  # Redirect back to the same page
    else:
        form = BookForm()
    books = Book.objects.all()  # Retrieve all books to display
    return render(request, 'myApp/add_book.html', {'add_book_form': form, 'books': books})

# View to delete a book
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()  # Delete the book from the database
        return redirect('add_book')  # Redirect to the add_book page after deletion
    return redirect('add_book')

# View to update a book
def update_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()  # Save the updated book to the database
            return redirect('add_book')  # Redirect after saving
    else:
        form = BookForm(instance=book)  # Pre-populate form with the book data
    return render(request, 'myApp/update_book.html', {'form': form, 'book': book})

# Register view (with registration functionality)
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Create a new user
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')  # Redirect to the login page
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserCreationForm()
    
    return render(request, 'myApp/register.html', {'form': form})

# myApp/views.py
from django.shortcuts import render, redirect
from .forms import NoteForm
from .models import Note

def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new note to the database
            return redirect('note_list')  # Redirect to a page showing all notes (adjust URL name as needed)
    else:
        form = NoteForm()
    
    return render(request, 'create_note.html', {'form': form})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm

# List all notes
def list_notes(request):
    notes = Note.objects.all()
    return render(request, 'list_notes.html', {'notes': notes})

# Create a new note
def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_notes')
    else:
        form = NoteForm()
    return render(request, 'create_note.html', {'form': form})

# Update an existing note
def update_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('list_notes')
    else:
        form = NoteForm(instance=note)
    return render(request, 'update_note.html', {'form': form, 'note': note})

# Delete a note
def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'POST':
        note.delete()
        return redirect('list_notes')
    return render(request, 'delete_note.html', {'note': note})

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # Ensure you have a 'home.html' template
