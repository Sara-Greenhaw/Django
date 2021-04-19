import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learning_log.settings')

import django 
django.setup()

from MainApp.models import Topic, Entry

topics = Topic.objects.all()

t = Topic.objects.get(id=1) #gets us chess, can look up on sql db browser lite, single topic

print(t)

entries = t.entry_set.all() #giving all entries related to the one topic
#whatever the name of the model, lowercase then _set.all()

for entry in entries:
    print(entry)

"""
for t in topics:
    print(f'Topic ID: {t.id}    Topic: {t}')

entries = Entry.objects.all()

for e in entries:
    print(f'Topic: {e.topic}')
    print(f'Text: {e}') #first 50 characters of post as specified in models
    print(f' Date Added: {e.date_added}')
"""