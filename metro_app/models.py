from django.db import models

# Create your models here.


class SellTicket(models.Model):
    source = models.CharField(max_length=50)
    destinationto = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    date = models.DateField()
