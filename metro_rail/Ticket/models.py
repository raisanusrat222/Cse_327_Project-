from django.db import models
# Create your models here.
class TrainFare(models.Model):
    """
       This class is used to create the Train Fare Objects. Has information regarding train source, destination, name, fare.

       This class is extended from the Model class ,so it has all the functionality
       of the model class.

       This class is used to create objects for database entry
       """
    trainid = models.IntegerField(primary_key=True)
    trainname = models.CharField(max_length=70)
    trainsource = models.CharField(max_length=70)
    traindestination = models.CharField(max_length=70)
    trainarrival = models.TimeField()
    trainreach = models.TimeField()
    trainfare = models.IntegerField(unique=True,null=True)

class Complain(models.Model):
    """
       This class is used to create the Complains from user. Stores ComplainNo,details of complainer and text of complain.

       This class is extended from the Model class ,so it has all the functionality
       of the model class.
,
       This class is used to create objects for database entry

    """
    ComplainNo = models.AutoField(primary_key=True)
    Complainer = models.CharField(max_length=100)
    Contact = models.CharField(max_length=100)
    Complain = models.TextField()

class TicketSell(models.Model):
    """
       This class is used to create the Ticket Sell. Stores all objects of sold ticket online.

       This class is extended from the Model class so it has all the functionality
       of the model class.

       This class is used to create objects for database entry

    """
    ticketNo = models.IntegerField(primary_key=True)
    ticketSource = models.CharField(max_length=70)
    ticketDestination = models.CharField(max_length=70)
    date = models.DateField()
    noOfTicket = models.IntegerField()
    total = models.IntegerField()
    email = models.EmailField()