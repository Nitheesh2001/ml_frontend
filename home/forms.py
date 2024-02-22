from django import forms
from .models import Cadidate

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Cadidate
        fields = ['cadidate_name', 'pdf_file', 'candidate_id']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pdf_file'].label = 'Upload Your CV' 