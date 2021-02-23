from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# class Profile(models.Model):
#     GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'))
#     user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='用户')
#     gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name='性别')  # 性别
#     birth_date = models.DateField(null=True, blank=True, verbose_name='出生日期')  # 出生日期
#     tel_number = models.CharField(max_length=11)
