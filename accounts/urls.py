from django.urls import path
from django.conf.urls import url
from . import views
# from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm


app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('choose/', views.chooser, name='choose'),
    # path('reset-password/', password_reset, name='reset_password'),
    # path('reset-password/done/', password_reset_done, name='password_reset_done'),
    # url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, name='password_reset_confirm'),

]
