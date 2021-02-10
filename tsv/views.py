from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.utils import timezone

from .forms import *
from .models import Answers
from .models import Profile

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

@login_required(login_url='common:login')
def my_page(request) :
    person, create = Profile.objects.get_or_create(user=request.user)
    return render(request, 'tsv/my_page.html', {'person' : person})

@login_required(login_url='common:login')
def edit_profile(request) :
    if request.method == 'POST' :
        user_change_form = CustomUserChangeForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_change_form.is_valid() and profile_form.is_valid() :
            user_change_form.save()
            profile = profile_form.save(commit=False)
            profile.image = request.FILES['profile_image']
            profile.save()
            return redirect('tsv:my_page')
        return redirect('tsv:edit_profile')
    else:
        user_change_form = CustomUserChangeForm(instance=request.user)
        profile, create = Profile.objects.get_or_create(user=request.user)
        profile_form = ProfileForm(instance=profile)
        context = {'user_change_form' : user_change_form, 'profile_form' : profile_form, 'person' : profile }
        return render(request, 'tsv/edit_profile_form.html', context)