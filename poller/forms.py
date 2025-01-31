from django import forms
from .models import Game, Vote

class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = ['game']
