from django.contrib import admin

# Register your models here.
from dailyLog.models import Diaries, Inspirations

admin.site.register(Diaries)
admin.site.register(Inspirations)