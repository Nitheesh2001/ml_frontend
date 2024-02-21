from django import forms
from .models import Cadidate

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Cadidate
        fields = ['cadidate_name', 'pdf_file', 'candidate_id']
