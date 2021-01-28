from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view
from rest_framework import status
from journals.models import Journal
from django.contrib.auth.models import User
from journals.serializers import JournalSerializer
from rest_framework.viewsets import ViewSet


class JournalViewSet(ViewSet):
    
    def list(self, request):
        print(request.user)
        journals = Journal.objects.all()
        print(journals)
        serializer = JournalSerializer(journals)

        if len(journals) == 0: 
            return Response([])
        else:
            return Response(serializer.data)

    def create(self, request):
        permission_classes = [AllowAny]
        print(request.data['title'])
        print(request.data['content'])

        if not request.data['title'] or not request.data['content']:
            return Response({'message': 'title or content cannot be null'}, status.HTTP_400_BAD_REQUEST)
        
        newJournal = Journal(title=request.data['title'], content=request.data['content'])
        newJournal.save()

        serializer = JournalSerializer(newJournal)
        return Response(serializer.data, status.HTTP_201_CREATED)

# @api_view(['GET'])
# def getAllJournals(request):
#     print(request.user)
#     journals = Journal.objects.all()
#     serializer = JournalSerializer(journals)

#     if len(journals) == 0: 
#         return Response([])
#     else:
#         return Response(serializer.data)

# @api_view(['POST'])
# def addJournal(request):
#         print(request.title)
#         print(request.content)
#         return Response([])