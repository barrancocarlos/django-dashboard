from django.urls import path
from django.views.generic import TemplateView
from sensors import views

urlpatterns = [    
    path('', views.home, name='home'),
    path('blank-page/', views.blank, name='blank'), 
    path('temp-table/', views.temperatureList, name='temp-table'),
    path('temp-add/', views.temperatureCreate, name='temp-add'),
    path('temp-update/<int:id>/', views.temperatureUpdate, name='temp-update'),    
    path('temp-single/<int:id>/', views.temperatureListOne, name='temp-single'),        
]