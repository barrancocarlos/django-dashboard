from django.db import models

# Create your models here.

class Temperature(models.Model):
  value = models.IntegerField(max_length=200, default='00')
  creation_date = models.DateTimeField(auto_now_add=True)
  
  
  
  def __str__(self):
        return self.value
