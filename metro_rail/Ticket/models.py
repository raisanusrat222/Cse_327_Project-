from django.db import models
# Create your models here.
class TrainFare(models.Model):
    trainid = models.IntegerField(primary_key=True)
    trainname = models.CharField(max_length=70)
    trainsource = models.CharField(max_length=70)
    traindestination = models.CharField(max_length=70)
    trainarrival = models.TimeField()
    trainreach = models.TimeField()
    trainfare = models.IntegerField(unique=True,null=True)

class Complain(models.Model):
    ComplainNo = models.AutoField(primary_key=True)
    Complainer = models.CharField(max_length=100)
    Contact = models.CharField(max_length=100)
    Complain = models.TextField()

class TicketSell(models.Model):
    ticketNo = models.IntegerField(primary_key=True)
    ticketSource = models.CharField(max_length=70)
    ticketDestination = models.CharField(max_length=70)
    date = models.DateField()
    noOfTicket = models.IntegerField()
    total = models.IntegerField()
    email = models.EmailField()