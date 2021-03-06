from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.utils import timezone

from ..forms import *
from ..models import Answers

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

@login_required(login_url='common:login')
def answers_wake_up(request) :
    date = f'{datetime.now().year}-{datetime.now().month}-{datetime.now().day}'
    answer, is_exists = Answers.objects.get_or_create(username_id=request.user.id, answer_date=date)
    if request.method == 'POST':
        form = WakeUpForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.cm_answer_date = timezone.now()
            answer.save()
            return redirect('tsv:answers_did_well')
    else:
        form = WakeUpForm(instance=answer)
    context = {'form': form}
    return render(request, 'tsv/wake_up_form.html', context)

@login_required(login_url='common:login')
def answers_did_well(request) :
    date = f'{datetime.now().year}-{datetime.now().month}-{datetime.now().day}'
    answer, is_exists = Answers.objects.get_or_create(username_id=request.user.id, answer_date=date)
    if request.method == 'POST':
        form = DidWellForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.cm_answer_date = timezone.now()
            answer.save()
            return redirect('tsv:answers_happiness')
    else:
        form = DidWellForm(instance=answer)
    context = {'form': form}
    return render(request, 'tsv/did_well_form.html', context)

@login_required(login_url='common:login')
def answers_happiness(request) :
    date = f'{datetime.now().year}-{datetime.now().month}-{datetime.now().day}'
    answer, is_exists = Answers.objects.get_or_create(username_id=request.user.id, answer_date=date)
    if request.method == 'POST':
        form = HappinessForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.cm_answer_date = timezone.now()
            answer.save()
            return redirect('tsv:answers_meal')
    else:
        form = HappinessForm(instance=answer)
    context = {'form': form}
    return render(request, 'tsv/happiness_form.html', context)

@login_required(login_url='common:login')
def answers_meal(request) :
    date = f'{datetime.now().year}-{datetime.now().month}-{datetime.now().day}'
    answer, is_exists = Answers.objects.get_or_create(username_id=request.user.id, answer_date=date)
    if request.method == 'POST':
        form = MealForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.cm_answer_date = timezone.now()
            answer.save()
            return redirect('tsv:index')
    else:
        form = MealForm(instance=answer)
    context = {'form': form}
    return render(request, 'tsv/meal_form.html', context)