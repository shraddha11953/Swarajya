from django import forms
from .models import HelpOffer, HelpRequest

class HelpOfferForm(forms.ModelForm):
    class Meta:
        model = HelpOffer
        fields = ['help_type', 'description']

class HelpRequestForm(forms.ModelForm):
    class Meta:
        model = HelpRequest
        fields = ['description', 'location', 'image']
