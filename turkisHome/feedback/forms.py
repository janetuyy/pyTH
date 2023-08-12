from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'phone', 'message']
        # labels = {'name': 'name', 'phone': 'phone', 'message': 'message', 'time': 'time_create', 'user': 'user'}