from django import forms
from django.contrib.auth.forms import UserChangeForm
from tsv.models import Answers, Profile
from django.contrib.auth.models import User

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
class DidWellForm(forms.ModelForm) :
    class Meta :
        model = Answers
        fields = ['did_well']

        labels = {
            'did_well' : '가장 잘한 일',
        }
class HappinessForm(forms.ModelForm) :
    class Meta :
        model = Answers
        fields = ['happiness']

        labels = {
            'happiness' : '가장 행복했던 일',
        }
class MealForm(forms.ModelForm) :
    class Meta :
        model = Answers
        fields = {
            'breakfast' : '아침',
            'lunch' : '점심',
            'dinner' : '저녁',
        }
class CustomUserChangeForm(UserChangeForm) :
    password = None
    username = forms.CharField(label="username", max_length=15, required=False)
    class Meta :
        model = User
        fields = ['email', 'username']
class ProfileForm(forms.ModelForm) :
    nickname = forms.CharField(label="nickname", max_length=15, required=False)
    image = forms.ImageField(label="profile_image", required=False)
    class Meta :
        model = Profile
        fields = ['nickname', 'image']