from django.shortcuts import render
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    """学习笔记的主页"""
    return render(request, 'learning_log/index.html')


@login_required
def topics(request):
    """显示所有的主题"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_log/topics.html', context)


@login_required
def topic(request, topic_id):  # 接收正则表达式捕获的值并存储到topic_id中
    """显示单个主题及所有的条目"""
    topic = Topic.objects.get(id=topic_id)  # 使用get()来获取指定的主题
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')  # 获取与该主题相关联的条目并将它们按date_added排序，前面的-号指按降序排列
    context = {'topic': topic, 'entries': entries}  # 将主题和条目都存储在字典中，再将这个字典发送给模板topic.html
    return render(request, 'learning_log/topic.html', context)


@login_required
def new_topic(request):
    """添加新主题"""
    # 从服务器读取数据的页面使用GET请求，用户需要通过表单提交信息时，使用POS请求
    if request.method != 'POST':
        # 未提交数据：创建一个新表单
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():  # 如果信息是有效的，保存到数据库
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(
                reverse(
                    'learning_log:topics'))  # 用reverse获取页面topics的URL，将其传递给HttpResponseRedirect(),后者将用户的浏览器重定向到页面Topics
    context = {'form': form}  # 通过上下文将这个表单发送给模板
    return render(request, 'learning_log/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """在特定的主题中添加新条目"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_log:topic', args=[topic_id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_log/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """编辑既有条目"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_log:topic', args=[topic.id]))
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_log/edit_entry.html', context)
