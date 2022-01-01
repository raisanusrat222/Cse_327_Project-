from django.db import models
from datetime import  date


class schedule_check (models.Model):
    """
    This class is used to create schedule of metro rail
    This class is extended from the Model class so it has all the functionality
    of the model class.
    
    this class is used to create objects for database entry has fields called route_id,source,destination,arrival_time,departure_time
    """
    route_id=models.CharField(max_length=200, null=True)
    source= models.CharField(max_length=200, null=True)
    destination=models.CharField(max_length=200, null=True)
    arrival_time=models.TimeField(null=True)
    departure_time=models.TimeField(null=True)

class user_ticket (models.Model):
    """
    This class is used to store ticket information of users.
    This class is extended from the Model class so it has all the functionality
    of the model class.
    
    this class is used to create objects for database entry has fields called ticket_no,date,email,no_of_tickets,total
    """
    
    ticket_no=models.IntegerField(default=0)
    source= models.CharField(max_length=200, null=True)
    destination=models.CharField(max_length=200, null=True)
    date= models.DateField() 
    email=models.EmailField(max_length=255,default='example@email.com')
    no_of_tickets=models.IntegerField(default=0)
    total=models.IntegerField(default=0)
    


    

class employee_ticket(models.Model):
    """
    This class is used to store ticket information of employee.
    This class is extended from the Model class so it has all the functionality
    of the model class.
    
    this class is used to create objects for database entry has fields called ticket_no,date,no_of_tickets,total
    """
    ticket_no=models.IntegerField(default=0)
    source= models.CharField(max_length=200, null=True)
    destination=models.CharField(max_length=200, null=True)
    date= models.DateField()
    no_of_tickets=models.IntegerField(default=0)
    total=models.IntegerField(default=0)



     
    
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
    Start_Date = models.DateField(auto_now=True)  
    Card_Status = models.CharField(max_length=15, default='',null=True)  
     
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