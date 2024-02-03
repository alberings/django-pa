# spinning_wheel/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('wheel/', views.wheel_view, name='wheel'),  # The 'wheel_view' function should be defined in views.py
]