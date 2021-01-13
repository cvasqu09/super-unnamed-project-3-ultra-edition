from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from books.models import Book
from books.serializers import BookSerializer


class BookViewSet(ViewSet):
    # TODO: Change to retrieve books for a given user
    def list(self, request):
        books = Book.objects.all()

        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
