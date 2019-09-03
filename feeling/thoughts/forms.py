from django import forms
from .models import Thought

class ThoughtForm(forms.ModelForm):
    class Meta:
        fields= ('condition','notes')
        model= Thought