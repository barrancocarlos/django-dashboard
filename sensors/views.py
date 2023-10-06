from django.shortcuts import render
from django.views.generic import TemplateView # Import TemplateView
from .models import Temperature

# Create your views here.

def home(request):
	return render(request, "index.html", {})

def blank(request):
	return render(request, "blank.html", {})

def temperatureList(request):  
    temperatures = Temperature.objects.all()      
    return render(request,"temp-table.html", {'temperatures': temperatures}) 
