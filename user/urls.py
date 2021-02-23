from django.contrib.auth.views import LoginView
from django.urls import path
from .views import *

urlpatterns = [
    # path('showUser/', showUser_views),
    path('login/', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
]
