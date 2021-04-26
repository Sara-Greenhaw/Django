from django.urls import path
from . import views 

app_name = 'MainApp'

#defining different url pages we want
#blank is the home page
#access function called index in our views file
urlpatterns = [
    path('', views.index, name='index'), #homepage
    path('topics', views.topics, name='topics'), #urls.py file
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
]


        



#anytime create new page, 
# urls.py specify addy or location of webpage along w view of location --> urls in app folder pertaining to this particular app
# views.py write funciton to interact w database
#template html file to write code to display