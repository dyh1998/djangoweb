from django.contrib import admin

# Register your models here.
# 向管理网站注册Topic
from learning_log.models import Topic, Entry

# 导入要注册的模型
admin.site.register(Topic)
# 让Django通过管理网站管理模型
admin.site.register(Entry)
