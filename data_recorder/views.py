from urllib import response
from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
from .forms import JBForm
from django.http import HttpResponseRedirect
from django.http import FileResponse
import io

from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter, A4
#from .reportlab_script import NCR_report
# Create your views here.

#def home(request): #"request" or "response" are always used as the parameter in django functions, in this case we return a response
#    return render(request, 'data_recorder/home.html')


def home(request):
    # context = {
    #     'posts': Post.objects.all()
    # }
    return render(request, 'data_recorder/pdf_generate.html')


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
        if 'submitted' in request.GET: # if we are in the GET request, subm variable becomes true
            subm = True
        
    form = JBForm
    return render(request, 'data_recorder/form_page.html', {'form' : form, 'subm_key':subm}) # connects to html page here


# def test(request):
#       theObj = NCR_report(A4)

#       return theObj






