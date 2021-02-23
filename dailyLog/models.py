from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Diaries(models.Model):
    weather = models.CharField(max_length=8, verbose_name='天气')
    mood = models.CharField(max_length=8, verbose_name='心情')
    event = models.CharField(max_length=30, verbose_name='事件')
    process = models.TextField(verbose_name='过程')
    date_created = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='拥有者', default=1)

    class Meta:
        verbose_name = '日记'
        verbose_name_plural = verbose_name
        ordering = ['date_created']

    def __str__(self):
        return self.event


class Inspirations(models.Model):
    topic = models.CharField(max_length=30, verbose_name='主题')
    detail = models.TextField(verbose_name='细节')
    date_created = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='拥有者', default=1)

    class Meta:
        verbose_name = '灵感'
        verbose_name_plural = verbose_name
        ordering = ['date_created']

    def __str__(self):
        return self.topic