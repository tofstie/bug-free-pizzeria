from django.urls import path, include
from . import views
from django.contrib import admin
app_name = 'users'
admin.autodiscover()
urlpatterns = [
    path('',include('django.contrib.auth.urls')),
    path('log_out', views.log_out, name='log_out'),
    path('register/', views.register, name='register')
]