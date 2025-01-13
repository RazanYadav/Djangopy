from django.contrib import admin
from myApp.models import Book # type: ignore

# Register your models here.
admin.site.register(Book)
