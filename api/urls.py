from django.urls import path
from api import views

urlpatterns = [
    path('api/words', views.word_list),
    path('api/words/<int:pk>/', views.word_detail),
    path('api/words/<int:pk>/video', views.video_list)
]
