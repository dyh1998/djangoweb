from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

# from user.models import Profile


# post_save使得User模型在save方法发出后会调用注册的方法，
# 调用receiver对其进行装饰
# @receiver(post_save, sender=User)
# # 创建用户档案
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:  # 创建用户档案
#         Profile.objects.create(user=instance)
#
#
# @receiver(post_save, sender=User)
# # 保存用户档案
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()  # 保存用户档案
#
#
# def showUser_views(request):
#     # user = User.objects.get(id=id)
#     # return render(request, 'user/showUser.html', locals())
#     return HttpResponse('123')


def logout_view(request):
    """注销用户"""
    logout(request)
    return HttpResponseRedirect(reverse('learning_log:index'))


def register(request):
    """注册新用户"""
    if request.method != 'POST':
        # 显示空的注册表单
        form = UserCreationForm()
    else:
        # 处理填写好的表单
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # 让用户自动登录，再重定向到主页
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_log:index'))
    context = {'form': form}
    return render(request, 'user/register.html', context)
