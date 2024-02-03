from django import forms
from .models import WheelItem

class WheelItemForm(forms.ModelForm):
    class Meta:
        model = WheelItem
        fields = ['name']
