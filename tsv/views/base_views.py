from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from ..models import Answers

@login_required(login_url='common:login')
def index(request) :
    return render(request, 'tsv/index.html')

@login_required(login_url='common:login')
def detail(request, answers_id) :
    answers = get_object_or_404(Answers, pk=answers_id)
    if request.user.id != answers.username_id :
        messages.error(request, '확인할 권한이 없습니다.')
        return redirect('tsv:my_page')
    context = {'answers' : answers}
    return render(request, 'tsv/detail.html', context)