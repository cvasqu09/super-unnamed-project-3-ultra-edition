from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view
from books.models import Book, Shelf
from books.serializers import BookSerializer


class BookViewSet(ViewSet):
    # TODO: Change to retrieve books for a given user
    def list(self, request):
        books = Book.objects.all()

        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def getBooks(request):
    readFilter = Shelf.READ
    if request.method == 'GET' and 'filter' in request.GET:
        filterParam = request.GET['filter']
        if filterParam in Shelf.SHELF_STATUSES.keys():
            readFilter = Shelf.SHELF_STATUSES[filterParam]
    
    
    
    books = Book.objects.filter(shelf=readFilter)

    serializer = BookSerializer(books, many=True)
    return Response(serializer.data[:20])