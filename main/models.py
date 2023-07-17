from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

class CleaningService(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name

class Booking(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    cleaning_service = models.ForeignKey(CleaningService, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    time = models.TimeField(default=timezone.now().strftime('%H:%M'))  
    duration = models.PositiveIntegerField()
    name = models.CharField(max_length=255,default='name')

    def __str__(self):
        return f"Booking #{self.id} - Customer: {self.customer.username}"







    


   

    

    