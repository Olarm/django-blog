from django.urls import path
from . import views


urlpatterns = [
    #127.0.0.1:8000 sendes direkte til post_list
    path('', views.post_list, name='post_list'),
]
