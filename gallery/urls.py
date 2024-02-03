# Inside your app's urls.py (e.g., gallery/urls.py)

from django.urls import path
from .views import photo_upload, gallery

urlpatterns = [
    path('upload/', photo_upload, name='photo_upload'),
    path('gallery/', gallery, name='gallery'),
]
