from django import forms
from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    """继承自froms的ModelForm"""

    class Meta:
        # 内嵌的类告诉FDjango根据哪个模型创建表单，以及在表单中包含哪些字段
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
