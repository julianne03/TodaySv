from django.shortcuts import render, get_object_or_404, redirect
from .models import Answers
from .forms import AnswersForm

def index(request) :
    return render(request, 'tsv/index.html')

def answers_create(request) :
    if request.method == 'POST' :
        form = AnswersForm(request.POST)
        if form.is_valid() :
            answers = form.save(commit=False)
            answers.weather = request.GET()
            answers.save()
            return redirect('tsv:index')
    else:
        form = AnswersForm()
    context = {'form':form}
    return render(request, 'tsv/answers_form.html', context)