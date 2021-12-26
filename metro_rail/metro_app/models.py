from django.db import models
from datetime import datetime, date

class schedule_check (models.Model):
    route_id=models.CharField(max_length=200, null=True)
    source= models.CharField(max_length=200, null=True)
    destination=models.CharField(max_length=200, null=True)
    arrival_time=models.TimeField()
    departure_time=models.TimeField()

class user_ticket (models.Model):
    
    train_no=models.IntegerField(default=0)
    source= models.CharField(max_length=200, null=True)
    destination=models.CharField(max_length=200, null=True)
    date= models.DateField() 
    email=models.EmailField(max_length=255,default='example@email.com')
    no_of_tickets=models.IntegerField(default=0)
    total=models.IntegerField(default=0)
    

class premium_ticket(models.Model):
    first_name = models.CharField(max_length=30,default='',null=False)       
    last_name = models.CharField(max_length=30,default='',null=False)
    user_name = models.CharField(max_length=30,default='',null=False)
    phone_number = models.CharField(max_length=30,default='',null=False)
    nid = models.CharField(max_length=30,default='',null=False)
    package = models.CharField(max_length=30, default='', null=False)
    start_date = models.DateField()      
    pay_with = models.CharField(max_length=30)       
    card_num = models.CharField(max_length=30,default='',null=False)
    card_status = models.CharField(max_length=15, default='')  
     
    
     
     
       