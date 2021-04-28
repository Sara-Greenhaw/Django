from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Topic(models.Model): 
    #this is a text field we can enter in a topic
    text = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add = True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.text
        #returning back actual text of the topic, the name of the topic which is the field
        #if you didnt have this, the my shell run would return text object


class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return f'{self.text[:50]}...'


