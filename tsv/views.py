from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.utils import timezone

from .models import Answers
from .forms import WeatherForm, MoodForm

@login_required(login_url='common:login')
def index(request) :
    return render(request, 'tsv/index.html')

@login_required(login_url='common:login')
def answers_weather(request) :
    #만약 해당하는 데이터가 없다면 밑에 실행 아니면 else -> 함수로 따로 빼기
    date = f'{datetime.now().year}-{datetime.now().month}-{datetime.now().day}'
    answer, is_exists = Answers.objects.get_or_create(username_id=request.user.id, answer_date=date)
    if request.method == 'POST':
        form = WeatherForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.cm_answer_date = timezone.now()
            answer.save()
            return redirect('tsv:answers_mood')
    else:
        form = WeatherForm(instance=answer)
    context = {'form': form}
    return render(request, 'tsv/weather_form.html', context)

@login_required(login_url='common:login')
def answers_mood(request) :
    date = f'{datetime.now().year}-{datetime.now().month}-{datetime.now().day}'
    answer, is_exists = Answers.objects.get_or_create(username_id=request.user.id, answer_date=date)
    if request.method == 'POST':
        form = MoodForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.cm_answer_date = timezone.now()
            answer.save()
            return redirect('tsv:answers_wake_up')
    else:
        form = MoodForm(instance=answer)
    context = {'form': form}
    return render(request, 'tsv/mood_form.html', context)