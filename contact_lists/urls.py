from django.urls import path, include
from . import views

urlpatterns = [
    path('callfire/', views.callfire, name = 'callfire')
]