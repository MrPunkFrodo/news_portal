from django.urls import path
from .views import PostsList, PostsDetail


urlpatterns = [
   path('posts/', PostsList.as_view()),
   path('<int:pk>', PostsDetail.as_view()),
]