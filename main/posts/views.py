from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from posts.models import Post
from posts.serializers import PostSerializer
from rest_framework.viewsets import ViewSet

class PostViewSet(ViewSet):
    # Retrieve list of posts by a given user
    def list(self, request):
        posts = Post.objects.filter(user_id=1)

        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
