from django.urls import path
from .views import *

urlpatterns = [
    path('show_diary/', showDiary_views, name='showDia'),
    path('newEdit_diary/', newEditDiary_views, name='newEditDia'),
    path('show_inspiration/', showInspiration_views, name='showIns'),
    path('newEdit_inspiration/', newEditInspiration_views, name='newEditIns')
]
