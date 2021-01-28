from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

@api_view(['POST'])
@permission_classes([AllowAny])
def createUser(request):
    username = request.data['username']
    first_name = request.data['firstName']
    last_name = request.data['lastName']
    password = request.data['password']

    user = User.objects.create_user(
        first_name=first_name,
        last_name=last_name,
        username=username,
        password=password)

    user.save()
    return Response(status.HTTP_201_CREATED)