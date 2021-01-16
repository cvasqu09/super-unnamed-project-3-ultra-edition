from rest_framework import serializers
from books.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'id', 
            'title', 
            'author', 
            'number_of_pages', 
            'year_published', 
            'original_publication',
            'isbn_13'
        ]