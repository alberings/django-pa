from django.urls import path
from .views import register, profile, custom_logout

urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('logout/', custom_logout, name='logout'),
]
