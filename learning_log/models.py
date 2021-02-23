from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length=200,verbose_name='科目')  # 由字符或文本组成的数据，需要存储少量的文本 定义CharFiled属性时需要告诉Django在该数据库预留多少空间，即max_length=200
    date_added = models.DateTimeField(auto_now_add=True)  # 记录日期和时间的数据，auto_now_add=True是让Django将这个属性自动设置成当前日期和时间
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='拥有者',default=1)

    class Meta:
        verbose_name = '科目'
        verbose_name_plural = verbose_name
        ordering = ['date_added']

    def __str__(self):  # 告诉Django默认使用那个属性来显示有关主题的信息，即__str__这个属性
        """返回模型的字符串表示"""
        return self.text


class Entry(models.Model):
    """学到的有关某个主题的具体知识"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name='知识点')  # 将每个条目关联到特定的主题,设置Entry为Topic外键
    text = models.TextField(verbose_name='笔记')  # 不限制文本长度
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '笔记'
        verbose_name_plural = verbose_name
        ordering = ['date_added']

    def __str__(self):  # 用此方法来告诉Django只显示text的前50个字符
        return self.text[:50] + '...'
