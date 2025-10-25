from django import forms
from .models import RapeReport

class RapeReportForm(forms.ModelForm):
    class Meta:
        model = RapeReport
        fields = ['title', 'description', 'location', 'date', 'image']
