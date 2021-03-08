from django.urls import path

from .views import *

urlpatterns = [
    path('show_titles/', index, name='titles'),
    path('post/<int:pk>/', detail, name='detail'),
    path('archives/<int:year>/<int:month>/', archive, name='archive'),
    path('categories/<int:pk>/', category, name='category'),
    path('tags/<int:pk>/', tag, name='tag'),
]
