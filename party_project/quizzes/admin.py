# quizzes/admin.py

from django.contrib import admin
from .models import Question
from .forms import QuestionAdminForm

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'quiz', 'correct_answer')
    form = QuestionAdminForm

    def correct_answer(self, obj):
        # Retrieve the correct answer for the question
        correct_answer = obj.answer_set.filter(is_correct=True).first()
        if correct_answer:
            return correct_answer.text
        return "No correct answer"

    correct_answer.short_description = 'Correct Answer'
