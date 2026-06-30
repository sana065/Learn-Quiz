from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_file, name='upload'),
    path('quiz/', views.quiz_page, name='quiz'),
    path('results/', views.results, name='results'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
]