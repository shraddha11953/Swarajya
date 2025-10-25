from django import forms
from .models import CorruptionReport

class CorruptionReportForm(forms.ModelForm):
    class Meta:
        model = CorruptionReport
        fields = ['title', 'description', 'location', 'date', 'proof_image']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }
