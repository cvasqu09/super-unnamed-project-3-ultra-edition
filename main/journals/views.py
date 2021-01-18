from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
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
            return Response([{'title': 'test'}])
        else:
            return Response(serializer.data)