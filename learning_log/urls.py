# 当前的URL文件位于下面注释中的文件中
"""定义learning_logs的URL模式"""
# 导入函数url将URL映射到试图
from django.conf.urls import url
from django.urls import path
# 导入views模块，其中的句点是让python从当前文件夹中导入视图
from . import views

# 包含可在应用程序learning_logs中请求的网页
urlpatterns = [
    # 主页
    # 添加代码来包含模块learning_logs，namespace是为了让learning_log的URL中的其他URL区分开来
    # 函数接收3个实参，第一个是正则表达式，找开头和结尾之间没有任何东西的URL，
    # 第二个实参指定了要调用的视图函数
    # 第三个实参将这个URL模式的名称指定为index，依此让我们在代码的其他地方引用它
    path('', views.index, name='index'),
    # 显示所有的主题
    path('topics/', views.topics, name='topics'),
    path('topic/(<topic_id>)/', views.topic, name='topic'),  # 与包含在两个斜杠内的整数匹配，#将捕获的值存储到topic_id中
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/(<topic_id>)/', views.new_entry, name='new_entry'),
    path('edit_entry/(<entry_id>)/', views.edit_entry, name='edit_entry'),
]
app_name = 'learning_log'
