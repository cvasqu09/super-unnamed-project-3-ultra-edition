from django.urls import path, include
from users import views
from rest_framework import routers
from users.views import UserViewSet
from posts.views import PostViewSet
from books.urls import urlpatterns
from books.views import getBookStats
from journals.views import JournalViewSet

router = routers.SimpleRouter()
router.register(r'users', UserViewSet, basename='User')
router.register(r'posts', PostViewSet, basename='Post')
router.register(r'journals', JournalViewSet, 'Journal')

statspatterns = [
    path('stats/books/', getBookStats)
]

urlpatterns = router.urls + urlpatterns + statspatterns
