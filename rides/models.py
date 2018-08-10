from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class FormBasic(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    birthdate = models.CharField(max_length=8)
    patient_med_number = models.CharField(max_length=30)
    number_of_passengers = models.IntegerField(default=1)
    appointment_date = models.CharField(max_length=15)
    pickup_time = models.CharField(max_length=10)
    return_time = models.CharField(max_length=10)
    pickup_address = models.CharField(max_length=30)
    destination_address = models.CharField(max_length=30)
    time_stamp = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,  on_delete=models.CASCADE, default=None)

    def __str__(self):
        return str(self.author)

class Reoccuring(models.Model):

    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    birthdate = models.CharField(max_length=8)
    patient_med_number = models.CharField(max_length=30)
    number_of_passengers = models.CharField(max_length=1)
    start_date = models.CharField(max_length=12)
    end_date = models.CharField(max_length=12)

    pickup_address_one = models.CharField(max_length=30, default="")
    destination_address_one = models.CharField(max_length=30, default="")
    pickup_time_one = models.CharField(max_length=12,default="")
    return_time_one =  models.CharField(max_length=12,default="")
    weekday_one =  models.CharField(max_length=12,default="")

    pickup_address_two = models.CharField(max_length=30, default="")
    destination_address_two = models.CharField(max_length=30, default="")
    pickup_time_two = models.CharField(max_length=12,default="")
    return_time_two =  models.CharField(max_length=12,default="")
    weekday_two =  models.CharField(max_length=12,default="")

    time_stamp = models.DateTimeField(editable=True, auto_now_add=True)
    author = models.ForeignKey(User,  on_delete=models.CASCADE, default=None)


    def __str__(self):
        return str(self.author)



    # pickup_time_three = models.CharField(max_length=12)
    # return_time_three =  models.CharField(max_length=12)
    # pickup_day_three =  models.CharField(max_length=12)
    #
    # pickup_time_four =  models.CharField(max_length=12)
    # return_time_four = models.CharField(max_length=12)
    # pickup_day_four =  models.CharField(max_length=12)
    #
    # pickup_time_five =  models.CharField(max_length=12)
    # return_time_five =  models.CharField(max_length=12)
    # pickup_day_five =  models.CharField(max_length=12)
    #
    # pickup_time_six = models.CharField(max_length=12)
    # return_time_six =  models.CharField(max_length=12)
    # pickup_day_six =  models.CharField(max_length=12)
    #
    # pickup_time_seven =  models.CharField(max_length=12)
    # return_time_seven =  models.CharField(max_length=12)
    # pickup_day_seven =  models.CharField(max_length=12)
