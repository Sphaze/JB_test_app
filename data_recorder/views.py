from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
from .forms import JBForm
from django.http import HttpResponseRedirect
# Create your views here.

#def home(request): #"request" or "response" are always used as the parameter in django functions, in this case we return a response
#    return render(request, 'data_recorder/home.html')

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'data_recorder/home.html', context)


def about(request):
    return render(request, 'data_recorder/about.html', {'title': 'About'})



def add_data(request):
    subm = False
    if request.method == "POST":
        form = JBForm(request.POST)
        if form.is_valid():
            form.save()
            return  HttpResponseRedirect('/?submitted=true') # if this html happens, it will be in the GET request
    else: 
        form = JBForm
        if 'submitted' in request.GET: # subm variable is normally false, if 'submitted' is true in the html, subm variable becomes true
            subm = True
        
    form = JBForm
    return render(request, 'data_recorder/form_page.html', {'form' : form, 'submitted':subm})


