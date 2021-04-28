from django.shortcuts import render, redirect
from django.contrib.auth import login 
from django.contrib.auth.forms import UserCreationForm 


# Create your views here.
#if its a get request, should load up empty form for user to put in username and pass
#submit button is post request, so take data and put in database

def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
        # empty form
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save() #we want to create the user and auto log them in as well
            #if just create user they still have to login after creating account
            login(request, new_user)
            return redirect('MainApp:index') #redirects to our index page AKA home page

    context = {'form':form}
    return render(request, 'registration/register.html', context)
