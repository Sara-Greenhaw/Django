from django.urls import path, include 

app_name = 'users'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
]
#using django default views so no need for separate views
#need templates folder and another folder called registration