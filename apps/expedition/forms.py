from django import forms
from .models import Expedition

class ExpeditionForm(forms.ModelForm):
    class Meta:
        model = Expedition
        fields = ["name", "goal", "description"]