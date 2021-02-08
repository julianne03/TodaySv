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
class WakeUpForm(forms.ModelForm) :
    class Meta :
        model = Answers
        fields = ['wake_up']

        labels = {
            'wake_up' : '일어난 시각',
        }