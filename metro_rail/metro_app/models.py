from django.db import models


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
    arrival_time=models.TimeField()
    departure_time=models.TimeField()

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
    

class premium_ticket(models.Model):
    """
    This class is used to store  information of premium users
    This class is extended from the Model class so it has all the functionality
    of the model class.
    
    this class is used to create objects for database entry has fields called first_name,last_name,user_name,phone_number,nid,package,start_date,pay_with,card_num,card_status
    """

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

class Employee(models.Model):
    """
    This class is used to store  information of employee
    This class is extended from the Model class so it has all the functionality
    of the model class.
    
    this class is used to create objects for database entry has fields called First_Name,Last_Name,User_Name,Phone_Number,NID,Address
    """
    First_Name = models.CharField(max_length=30,default='',null=False)       
    Last_Name = models.CharField(max_length=30,default='',null=False)
    User_Name = models.CharField(max_length=30,default='',null=False)
    Phone_Number = models.CharField(max_length=30,default='',null=False)
    NID = models.CharField(max_length=30,default='',null=False)
    Address = models.CharField(max_length=30,default='',null=False)


     
    
     
     
       