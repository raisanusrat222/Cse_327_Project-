from django.db import models
from datetime import datetime, date


    
    
class PremiumMember(models.Model):
    """
       This class is used to create the premium member Objects. It has information regarding premium member 
       name, username, password, email, phone number, nid, package and payment info.

       This class is extended from the Model class ,so it has all the functionality
       of the model class.

       This class is used to create objects for database entry

    """
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
    """
       This class is used to create the employee Objects. It has information regarding employee 
       name, username, password, email, phone number, nid, address.

       This class is extended from the Model class ,so it has all the functionality
       of the model class.

       This class is used to create objects for database entry
       
    """
    First_Name = models.CharField(max_length=30,default='',null=False)       
    Last_Name = models.CharField(max_length=30,default='',null=False)
    User_Name = models.CharField(max_length=30,default='',null=False)
    Phone_Number = models.CharField(max_length=30,default='',null=False)
    NID = models.CharField(max_length=30,default='',null=False)
    Address = models.CharField(max_length=30,default='',null=False)