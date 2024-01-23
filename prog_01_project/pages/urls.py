from django.urls import path
from pages import views

urlpatterns = [
    path('index', views.index, name='index'),
]