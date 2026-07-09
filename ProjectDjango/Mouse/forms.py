from django import forms
from .models import variety

class VarietyForm(forms.Form):
    variety = forms.ModelChoiceField(queryset=variety.objects.all(), label="Select Variety")
    