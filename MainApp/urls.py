from django.urls import path

from . import views 

app_name = 'MainApp'

#defining different url pages we want
#blank is the home page
#access function called index in our views file
urlpatterns = [
    path('', views.index, name='index'),
]