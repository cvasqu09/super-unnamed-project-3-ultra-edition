from django.urls import path, include
from users import views
from rest_framework import routers
from users.views import UserViewSet
from posts.views import PostViewSet
from books.urls import urlpatterns

router = routers.SimpleRouter()
router.register(r'users', UserViewSet, basename='User')
router.register(r'posts', PostViewSet, basename='Post')

urlpatterns = router.urls + urlpatterns
