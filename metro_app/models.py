from django.db import models
from django.contrib.auth.models import User

# Create your models here.   

#Question model
class Question(models.Model):
   author = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
   title = models.CharField(max_length=200, null=False)
   body = models.TextField(null=False)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   def __str__(self):
       return self.title

class Answer(models.Model):
   user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
   question = models.ForeignKey(Question, null=False, on_delete=models.CASCADE)
   parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
   body = models.TextField(null=False)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now_add=True)

   def __str__(self):
       return self.body        


class SellTicket(models.Model):
    source = models.CharField(max_length=50)
    destinationto = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    date = models.DateField()

    def __str__(self):
       return self.email 





    
    




