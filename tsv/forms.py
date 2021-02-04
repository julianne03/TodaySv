from django import forms
from tsv.models import Answers

class AnswersForm(forms.ModelForm) :
    class Meta :
        model = Answers
        fields = ['weather']