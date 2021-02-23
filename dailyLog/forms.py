from django import forms

from .models import *


class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diaries
        fields = ('weather', 'mood', 'event', 'process')


class InspirationForm(forms.ModelForm):
    class Meta:
        model = Inspirations
        fields = ('topic', 'detail')
