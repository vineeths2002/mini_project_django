from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Master(models.Model):
    created_date=models.DateField(auto_now_add=True)
    is_active=models.BooleanField(default=True)

class events(Master):
    name=models.CharField(max_length=700)
    photos = models.ImageField(upload_to='events/')
    discription = models.TextField(max_length=800)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.name

class workers(Master):
    name=models.CharField(max_length=700)
    photos = models.ImageField(upload_to='events/')
    discription = models.TextField(max_length=800)
    phone_number=models.IntegerField(max_length=20)


    def __str__(self):
        return self.name

  
class Booking(Master):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.IntegerField(max_length=10)
    discription =models.TextField(max_length=500)
    booked_at = models.DateTimeField(auto_now_add=True)



   