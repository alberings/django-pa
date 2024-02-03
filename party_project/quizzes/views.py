# quizzes/views.py

from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from .models import Quiz, Question, Answer
from .forms import QuizForm, QuestionForm, AnswerForm
from django.contrib.auth.decorators import login_required
from .models import QuizSession
from django.urls import reverse
from .models import Quiz, Question, Answer


def add_answer(request, quiz_id, question_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    question = get_object_or_404(Question, pk=question_id, quiz=quiz)

    if request.method == 'POST':
        answer_form = AnswerForm(request.POST)
        if answer_form.is_valid():
            answer = answer_form.save(commit=False)
            answer.question = question
            answer.save()
            return redirect('add_answer', quiz_id=quiz_id, question_id=question_id)

    else:
        answer_form = AnswerForm()

    return render(request, 'quizzes/add_answer.html', {'quiz': quiz, 'question': question, 'answer_form': answer_form})

def create_quiz(request):
    if request.method == 'POST':
        quiz_form = QuizForm(request.POST)
        if quiz_form.is_valid():
            quiz = quiz_form.save(commit=False)
            quiz.owner = request.user
            quiz.save()
            return redirect('add_question', quiz_id=quiz.id)
    else:
        quiz_form = QuizForm()
    return render(request, 'quizzes/create_quiz.html', {'quiz_form': quiz_form})

def add_question(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    question = None

    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        if question_form.is_valid():
            question = question_form.save(commit=False)
            question.quiz = quiz
            question.save()
            return redirect('add_answer', quiz_id=quiz.id, question_id=question.id)

    else:
        question_form = QuestionForm()

    return render(request, 'quizzes/add_question.html', {'quiz': quiz, 'question_form': question_form, 'question': question})







# Similar views for adding answers and creating the quiz session.
@login_required
def calculate_score(quiz_id, user_answers):
    # Initialize the score
    score = 0
    
    # Get the quiz associated with the quiz_id
    quiz = Quiz.objects.get(pk=quiz_id)
    
    # Retrieve all the questions for the quiz
    questions = Question.objects.filter(quiz=quiz)
    
    # Iterate through the questions and check user's answers
    for question in questions:
        correct_answer = Answer.objects.get(question=question, is_correct=True)
        user_answer = user_answers.get(str(question.id))  # Get the user's answer for this question
        
        # Check if the user's answer matches the correct answer
        if user_answer == str(correct_answer.id):
            score += 1  # Add 1 point for each correct answer
    
    # Create a QuizSession to store the user's score
    QuizSession.objects.create(quiz_id=quiz_id, player=request.user, score=score)

def leaderboard(request, quiz_id):
    quiz_sessions = QuizSession.objects.filter(quiz_id=quiz_id).order_by('-score')
    return render(request, 'quizzes/leaderboard.html', {'quiz_sessions': quiz_sessions})


# quizzes/views.py

def play_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    questions = Question.objects.filter(quiz=quiz)
    user_answers = {}  # Dictionary to store user's answers
    score = 0

    if request.method == 'POST':
        # Handle user's answers and calculate score
        for question in questions:
            user_answer = request.POST.get(f'question_{question.id}')
            correct_answer = Answer.objects.get(question=question, is_correct=True)

            if user_answer == str(correct_answer.id):
                score += 1

            user_answers[question.id] = user_answer

        # Store the user's score in the session
        request.session['quiz_score'] = score

    return render(request, 'quizzes/play_quiz.html', {'quiz': quiz, 'questions': questions, 'user_answers': user_answers, 'score': score})

