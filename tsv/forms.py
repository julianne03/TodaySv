from django import forms
from tsv.models import Answers

class WeatherForm(forms.ModelForm) :
    class Meta :
        model = Answers
        fields = ['weather']

        labels = {
            'weather' : '날씨',
        }
class MoodForm(forms.ModelForm) :
    class Meta :
        model = Answers
        fields = ['mood']

        labels = {
            'mood' : '기분',
        }