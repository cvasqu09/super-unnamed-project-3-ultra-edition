from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view
from journals.models import Journal
from users.models import User
from journals.serializers import JournalSerializer
from rest_framework.viewsets import ViewSet


class JournalViewSet(ViewSet):
    
    def list(self, request):
        print(request.user)
        journals = Journal.objects.all()
        serializer = JournalSerializer(journals)

        if len(journals) == 0: 
            return Response([])
        else:
            return Response(serializer.data)

    def create(self, request):
        permission_classes = [AllowAny]
        print(request.data['title'])
        print(request.data['content'])
        return Response([])

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