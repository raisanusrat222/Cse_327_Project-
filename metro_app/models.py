from django.db import models

# Create your models here.
class sellticket(models.Model):
    destination_form = models.CharField(max_length=50)
    destination_to = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    travel_date = models.DateField()

    def __str__(self):
        return str(self.pk)+" "+ self.email+ " " + self.name