from django import forms

from .models import Challenge

class ChallengeForm(forms.ModelForm):
    class Meta:
        model = Challenge
        fields = ('title', 'description', 'challenge_status', 'challenge_start_date', 'challenge_end_date')