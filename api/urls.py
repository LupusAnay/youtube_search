from django.urls import path
from rest_framework.authtoken import views as auth_views
from api import views

urlpatterns = [
    path('api/words', views.word_list),
    path('api/words/<int:pk>/', views.word_detail),
    path('api/words/<int:pk>/video', views.video_list),
    path('api/auth', auth_views.obtain_auth_token)
]
