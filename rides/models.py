from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from multiselectfield import MultiSelectField


# Create your models here.

class FormBasic(models.Model):
    GENDER_CHOICES = (('Male','Male'),('Female','Female'))
    SERVICE_TYPES = (('SCFHP Basic','SCFHP Basic'),('VMC Basic','VMC Basic'))
    ACCOUNT_NUMBERS = (('SC00001','SC00001'),('I do not have one','I do not have one'))

    patient_first_name = models.CharField(max_length=50,default='')
    patient_last_name = models.CharField(max_length=50,default='')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES,default='Male')
    patient_phone = models.CharField(max_length=10)
    patient_birthdate = models.CharField(max_length=8)
    patient_med_number = models.CharField(max_length=30)
    number_of_passengers = models.PositiveIntegerField(default=1)
    appointment_date = models.CharField(max_length=15)
    round_trip = models.BooleanField(default=False)
    pickup_time = models.CharField(max_length=10,)
    return_time = models.CharField(max_length=10, blank=True, null=True )
    pickup_address = models.CharField(max_length=200)
    destination_address = models.CharField(max_length=200)
    account_number = models.CharField(max_length=30, choices=ACCOUNT_NUMBERS,default='')
    call_number = models.CharField(max_length=15,default='')
    service_type = models.CharField(max_length=15,choices=SERVICE_TYPES,default='')
    time_stamp = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,  on_delete=models.CASCADE, default=None)

    def __str__(self):
        return str(self.author)

class Reocurring(models.Model):
    DAY_CHOICES = (('Mon','Mon'),('Tue','Tue'),('Wed','Wed'),('Thur','Thur'),('Fri','Fri'),('Sat','Sat'),('Sun','Sun'))
    GENDER_CHOICES = (('Male', 'Male'),('Female', 'Female'))
    SERVICE_TYPES = (('SCFHP Basic','SCFHP Basic'),('VMC Basic','VMC Basic'))
    ACCOUNT_NUMBERS = (('SC00001','SC00001'),('I do not have one','I do not have one'))

    account_number = models.CharField(max_length=30, choices=ACCOUNT_NUMBERS,default='')
    call_number = models.CharField(max_length=15,default='')
    patient_first_name = models.CharField(max_length=30,default='')
    patient_last_name = models.CharField(max_length=30,default='')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES,default='Male')
    patient_phone = models.CharField(max_length=10)
    patient_birthdate = models.CharField(max_length=8)
    patient_med_number = models.CharField(max_length=30)
    number_of_passengers = models.PositiveIntegerField(default='1')
    service_type = models.CharField(max_length=15,choices=SERVICE_TYPES,default='')
    pickup_address = models.CharField(max_length=200 ,default='')
    destination_address = models.CharField(max_length=200,default='')
    pickup_time = models.CharField(max_length=12,default='')
    return_time =  models.CharField(max_length=12,default='')
    start_date = models.CharField(max_length=50,default='')
    end_date = models.CharField(max_length=50,default='')
    weekdays =  MultiSelectField(choices = DAY_CHOICES, default='')
    round_trip = models.BooleanField(default=False)

    time_stamp = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,  on_delete=models.CASCADE, default=None)

    def __str__(self):
        return str(self.author)
