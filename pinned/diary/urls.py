from django.conf.urls import url

from . import views
from django.urls import path

urlpatterns = [
    path('', views.base, name='base'),
    path('str/', views.store, name='store'),
    path('', views.draft_list, name='draft_list'),

]