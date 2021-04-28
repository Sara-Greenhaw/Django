from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
# Create your views here.
def index(request):
    ''' The home page for learning log. '''

    return render(request, 'MainApp/index.html')
    #going to use index.html file and render it with data

def topics(request):
    topics = Topic.objects.order_by('date_added') #sort order, default ascending, put minus for descending, all topics that are in database
    context = {'topics':topics} #these must match, the value has to be whatever object passing to website, this is a dictionary to pass to website while loading

    return render(request, 'MainApp/topics.html', context) #context of topics passed to topics.html

def topic(request, topic_id):
    topic = Topic.objects.get(id = topic_id)
    entries = topic.entry_set.order_by('-date_added') #descending order, getting from topic we have line above

    context = {'topic':topic, 'entries':entries} #passing multiple object through context dictionary to website

    return render(request, 'MainApp/topic.html', context)

def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)

        if form.is_valid():
            form.save()

            return redirect('MainApp:topics')
    context = {'form':form}
    return render(request, 'MainApp/new_topic.html', context)

def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)

        if form.is_valid():
            new_entry = form.save(commit=False)
            #when we have new entry, don't have associative topic for that entry, don't know which particular topic is connected to entry
            #this creates an instance called new entry with all information but false means dont save to database
            #assign topic to it then save it
            new_entry.topic = topic 
            new_entry.save()
            return redirect('MainApp:topic', topic_id=topic_id)

    context = {'form':form, 'topic':topic}
    return render(request, 'MainApp/new_entry.html', context)


def edit_entry(request, entry_id): 
    entry = Entry.objects.get(id = entry_id)
    topic = entry.topic 

    if request.method != 'POST': #meaning its get --> loading up what is exisitng
        form = EntryForm(instance = entry) #loads up an empty form, but don't want blank because we want it to be loaded with the info that is already there
        #getting entry from top of def edit_entry
    else:
        form = EntryForm(instance = entry, data = request.POST) #post request, whatever is in the form put to webpage
        if form.is_valid():
            form.save()
            return redirect('MainApp:topic', topic_id = topic.id) #to load up the topic page, need the topic ID, we have topic so topic.topicid gets up ID of that paritcular topic
    #context want to give entry, topic, and form
    context = {'entry':entry, 'topic':topic, 'form':form} #order does not matter
    return render(request, 'MainApp/edit_entry.html', context)