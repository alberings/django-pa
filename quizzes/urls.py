"""
URL configuration for quizzes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', views.create_quiz, name='create_quiz'),
    path('add_question/<int:quiz_id>/', views.add_question, name='add_question'),
    path('add_answer/<int:quiz_id>/<int:question_id>/', views.add_answer, name='add_answer'),
    path('play/<int:quiz_id>/', views.play_quiz, name='play_quiz'),
    path('leaderboard/<int:quiz_id>/', views.leaderboard, name='leaderboard'),
    path('list/', views.list_quizzes, name='list_quizzes'),
    path('delete/<int:quiz_id>/', views.delete_quiz, name='delete_quiz'),

    
]
