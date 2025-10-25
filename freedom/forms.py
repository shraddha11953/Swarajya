from django import forms
from .models import FreedomPost

class FreedomPostForm(forms.ModelForm):
    class Meta:
        model = FreedomPost
        fields = ['category', 'content', 'is_anonymous']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Write your opinion...'}),
        }
