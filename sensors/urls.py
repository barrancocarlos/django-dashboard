from django.conf.urls import url
from django.views.generic import TemplateView
from sensors import views

urlpatterns = [    
    url('^$', views.home, name='home'),   
]