from django.contrib import admin
from django.urls import path
from AppTwo import views

app_name = "AppTwo"

urlpatterns = [
    path('index/',views.index,name = 'index'),
    path('users/',views.users,name = 'users'),
    path('help/',views.help,name = 'help'),
    path('prfile/',views.userprofile,name = 'userprofile'),
]
