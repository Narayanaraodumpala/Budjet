from django import forms

from .models import *

class ConsultForm(forms.ModelForm):
    class Meta:
        model=Consults
        fields="__all__"