from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import *
from .models import *


# Create your views here.
@login_required
def showDiary_views(request):
    diarys = Diaries.objects.filter(owner=request.user).order_by('-date_created')
    return render(request, 'dailyLog/Diarys.html', locals())


@login_required
def newEditDiary_views(request):
    # diary = Diary.objects.get(id=diary_id)
    # if diaries.owner!=request.user:
    #     raise Http404
    if request.method != 'POST':
        form = DiaryForm()
    else:
        form = DiaryForm(request.POST)
        if form.is_valid():
            new_diary = form.save(commit=False)
            new_diary.owner = request.user
            new_diary.save()
            return HttpResponseRedirect(reverse('dailyLog:showDia'))
    return render(request, 'dailyLog/newDiarys.html', locals())


@login_required
def showInspiration_views(request):
    ins = Inspirations.objects.filter(owner=request.user).order_by('-date_created')
    return render(request, 'dailyLog/Inspirations.html', locals())


@login_required
def newEditInspiration_views(request):
    # ins = Inspiration.objects.get(id=inspiration_id)
    if request.method != 'POST':
        form = InspirationForm()
    else:
        form = InspirationForm(request.POST)
        if form.is_valid():
            new_diary = form.save(commit=False)
            new_diary.owner = request.user
            new_diary.save()
            return HttpResponseRedirect(reverse('dailyLog:showIns'))
    return render(request, 'dailyLog/newInspirations.html', locals())
