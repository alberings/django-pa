# quizzes/models.py

from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField  # If using PostgreSQL


class Quiz(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.TextField()

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

class QuizSession(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(default=0)
    answers = models.JSONField()  # Updated JSONField import
