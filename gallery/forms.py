# Inside your app's forms.py (e.g., gallery/forms.py)

from django import forms
from .models import Photo

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image']
