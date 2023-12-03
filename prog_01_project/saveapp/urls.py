from django.urls import path

from saveapp import views

urlpatterns = [
    path('', views.reload_data, name='reload_data' ),
]