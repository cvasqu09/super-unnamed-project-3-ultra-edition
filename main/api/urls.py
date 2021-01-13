from django.urls import path
from users import views
from rest_framework import routers
from users.views import UserViewSet
from posts.views import PostViewSet
from books.views import BookViewSet

router = routers.SimpleRouter()
router.register(r'users', UserViewSet, basename='User')
router.register(r'posts', PostViewSet, basename='Post')
router.register(r'books', BookViewSet, basename='Book')

urlpatterns = router.urls
