from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'rides'

urlpatterns = [
    # path('create', views.booking_create, name='create'),
    path('book', views.book_view, name='book'),
    path('multi', views.book_view_reoccuring, name='multi'),
    path('download', views.download_page, name='download'),
    url(r'^download/(?P<pk>\d+)$', views.download_page, name='download_with_pk'),
]
