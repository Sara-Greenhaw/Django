from django.urls import path, include 
#dot means from same folders (dot before vies)
from . import views
app_name = 'users'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
]
#using django default views so no need for separate views
#need templates folder and another folder called registration