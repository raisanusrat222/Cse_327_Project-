from django.db import models

class schedule_check (models.Model):
    route_id=models.CharField(max_length=200, null=True)
    source= models.CharField(max_length=200, null=True)
    destination=models.CharField(max_length=200, null=True)
    arrival_time=models.TimeField()
    departure_time=models.TimeField()

    
    
     
     
       