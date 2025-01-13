from django.urls import path
from . import views  # Import all views from the views.py file

urlpatterns = [
    # Login and Logout paths
    path('login/', views.login_view, name='login'),  # Login page
    path('logout/', views.logout_view, name='logout'),  # Logout functionality

    # Home page path
    path('', views.home, name='home'),  # Displays the home page with all books

    # Book management paths
    path('add/', views.add_book, name='add_book'),  # Add a new book
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),  # Delete a specific book
    path('update/<int:book_id>/', views.update_book, name='update_book'),  # Update a specific book

    # Register path
    path('register/', views.register, name='register'),  # Registration page

    # Notes management paths
    path('notes/', views.list_notes, name='list_notes'),
    path('notes/create/', views.create_note, name='create_note'),
    path('notes/<int:note_id>/update/', views.update_note, name='update_note'),
    path('notes/<int:note_id>/delete/', views.delete_note, name='delete_note'),
]
