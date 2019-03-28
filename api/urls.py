from django.urls import path
from rest_framework.authtoken import views as auth_views

from api import views

urlpatterns = [
    path('api/words', views.word_list),
    path('api/words/<int:pk>/', views.word_detail),
    # path('api/words/<int:pk>/video', views.video_list),
    # I don't actually know how to return detailed 404 messages
    # from generics.ListView, so video_list - without pagination, and
    # VideoListView without detailed 404 responses
    path('api/words/<int:pk>/video', views.VideoListView.as_view()),
    path('api/auth', auth_views.obtain_auth_token)
]
