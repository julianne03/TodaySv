from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from ..forms import *
from ..models import Answers
from ..models import Profile

@login_required(login_url='common:login')
def my_page(request) :
    person, create = Profile.objects.get_or_create(user=request.user)
    today = Answers.objects.filter(username_id=request.user.id)
    context = {'person' : person, 'today' : today}
    return render(request, 'tsv/my_page.html', context)

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