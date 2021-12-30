from django.db import models
from datetime import datetime, date


    
    
class PremiumMember(models.Model):
    First_Name = models.CharField(max_length=30,default='',null=False)       
    Last_Name = models.CharField(max_length=30,default='',null=False)
    User_Name = models.CharField(max_length=30,default='',null=False)
    Phone_Number = models.CharField(max_length=30,default='',null=False)
    NID = models.CharField(max_length=30,default='',null=False)
    Package = models.CharField(max_length=30, default='', null=False)        
    Pay_With = models.CharField(max_length=30)       
    Card_Num = models.CharField(max_length=30,default='',null=False)
    Start_Date = models.DateTimeField(auto_now=True)  
    Card_Status = models.CharField(max_length=15, default='')  
     
class Employee(models.Model):
    First_Name = models.CharField(max_length=30,default='',null=False)       
    Last_Name = models.CharField(max_length=30,default='',null=False)
    User_Name = models.CharField(max_length=30,default='',null=False)
    Phone_Number = models.CharField(max_length=30,default='',null=False)
    NID = models.CharField(max_length=30,default='',null=False)
    Address = models.CharField(max_length=30,default='',null=False)