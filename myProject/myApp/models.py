# myApp/models.py
from django.db import models

# models.py
from django.db import models

class Book(models.Model):
    bk_name = models.CharField(max_length=200)
    bk_number = models.IntegerField()
    bk_image = models.ImageField(upload_to='book_images/', blank=True, null=True)  # New field for the image

    def __str__(self):
        return self.bk_name


class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
# myApp/forms.py
from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']  # Specify which fields to include in the form
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter note title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter note content', 'rows': 5}),
        }



class Note(models.Model):
    title = models.CharField(max_length=100)  # Title of the note
    content = models.TextField()  # Content of the note
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for creation
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for last update

    def __str__(self):
        return self.title

