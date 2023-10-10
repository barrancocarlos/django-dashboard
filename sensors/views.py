from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView # Import TemplateView
from .models import Temperature

# Create your views here.

def home(request):
	return render(request, "index.html", {})

def blank(request):
	return render(request, "blank.html", {})

def temperatureList(request): 
    #Delete
    if request.POST: 
      if request.POST['action'] == "delete":  
        tempId = request.POST['temp_id'] 
        temperature = Temperature.objects.get(pk=tempId)   
        temperature.delete()
        return redirect(temperatureList)
    else:
      temperature = Temperature.objects.all()    
      temperatures = {'temperatures': temperature}     
      return render(request,"temp-table.html", temperatures)   
    
  
def temperatureCreate(request): 
  if request.POST: 
    newTemperature = Temperature()
    newTemperature.value = request.POST['value']
    newTemperature.save()
    return redirect(temperatureList)
  else:
    return render(request, "temp-add.html")    
  
def temperatureListOne(request, id):  
    temperature = Temperature.objects.get(id=id)   
    temperatures = {'temperatures': temperature}     
    return render(request,"temp-single.html", temperatures)  
  
def temperatureUpdate(request, id): 
  temperature = Temperature.objects.get(id=id)   
  temperatures = {'temperatures': temperature}   
  if request.POST: 
    tempId = request.POST['temp_id'] 
    updatedTemperature = Temperature.objects.get(pk=tempId) 
    updatedTemperature.value = request.POST['value']
    updatedTemperature.save()    
    return redirect(temperatureList)
  else:
    return render(request, "temp-update.html", temperatures)  
  

