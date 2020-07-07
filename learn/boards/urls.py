from django.urls import path
from . import views


urlpatterns = [
    path('', views.boardsHome, name='boardsHome'),
    path('<int:pk>/',views.boardTopics,name='boardTopics'),
    # re_path(r'^(?P<pk>\d+)$',views.boardTopics,name='boardTopics'),
    path('<int:pk>/new/',views.newTopic,name='newTopic'),
    path('<int:pk>/<int:pk2>/', views.postsFeed, name='postsList'),
    path('<int:pk>/<int:pk2>/new/', views.newPost, name='newPost'),
]
