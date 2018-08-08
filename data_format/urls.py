from django.urls import path
from . import views

app_name = 'data_format'

urlpatterns = [
    path('formatter', views.data_formatter, name='formatter'),

]
