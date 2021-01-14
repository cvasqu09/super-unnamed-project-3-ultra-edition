from django.urls import path, re_path, include
from books.views import getBooks

urlpatterns = [
    path('books/', getBooks)
]
