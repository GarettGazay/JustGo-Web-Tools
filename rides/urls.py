from django.urls import path
from . import views

app_name = 'rides'

urlpatterns = [
    # path('create', views.booking_create, name='create'),
    path('book', views.book_view, name='book'),
    path('multi', views.book_view_reoccuring, name='multi'),

]
