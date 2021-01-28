from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views
from posts.views import PostViewSet
from books.urls import urlpatterns
from books.views import getBookStats
from journals.views import JournalViewSet
from api.views import createUser

router = routers.SimpleRouter()
router.register(r'posts', PostViewSet, basename='Post')
router.register(r'journals', JournalViewSet, 'Journal')


statspatterns = [
    path('users/', createUser),
    path('stats/books/', getBookStats),
    path('auth/', views.obtain_auth_token, name='auth')
]

urlpatterns = router.urls + urlpatterns + statspatterns
