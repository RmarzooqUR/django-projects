from django.urls import path
from . import views


urlpatterns = [
    path('', views.boardsHome.as_view(), name='boardsHome'),
    path('<int:pk>/',views.boardTopics.as_view(), name='boardTopics'),
    # re_path(r'^(?P<pk>\d+)$',views.boardTopics,name='boardTopics'),
    path('<int:pk>/new/',views.newTopic, name='newTopic'),
    path('<int:pk>/<int:pk2>/', views.postsFeed.as_view(), name='postsList'),
    path('<int:pk>/<int:pk2>/new/', views.newPost, name='newPost'),
    path('<int:board_pk>/<int:topic_pk>/<int:post_pk>', views.EditPostView.as_view(), name='editPost')
]
