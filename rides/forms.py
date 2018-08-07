from django import forms
from . import models
from django.http import HttpResponse

class CreateBooking(forms.ModelForm):

    class Meta:
        model = models.FormBasic
        fields = ['name', 'phone','birthdate','patient_med_number','number_of_passengers','appointment_date','pickup_time','return_time', 'pickup_address', 'return_address']
        widgets = {
        'name' : forms.TextInput(attrs={'class' : 'form-control'}),
        'phone' : forms.TextInput(attrs={'class' : 'form-control'}),
        'birthdate' : forms.DateInput(attrs={'class' : 'form-control', 'placeholder' : 'This field SCFHP only'}),
        'patient_med_number' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'This field SCFHP only'}),
        'number_of_passengers' : forms.NumberInput(attrs={'class' : 'form-control'}),
        'appointment_date' : forms.TextInput(attrs={'class' : 'form-control'}),
        'pickup_time' : forms.TextInput(attrs={'class' : 'form-control'}),
        'return_time' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Leave blank if one way'}),
        'pickup_address' : forms.TextInput(attrs={'class' : 'form-control'}),
        'return_address' : forms.TextInput(attrs={'class' : 'form-control'}),
        }

class ReoccuringBooking(forms.ModelForm):

    class Meta:
        model = models.Reoccuring
        fields = ['name', 'phone','birthdate','patient_med_number','number_of_passengers','start_date','end_date','pickup_address_one','destination_address_one','pickup_time_one','return_time_one','weekday_one', 'pickup_address_two','destination_address_two','pickup_time_two','return_time_two','weekday_two', ]
        widgets = {
        'name' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Patient Name'}),
        'phone' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Patient Phone Number'}),
        'birthdate' : forms.DateInput(attrs={'class' : 'form-control', 'placeholder' : 'Patient Birthdate'}),
        'patient_med_number' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Patient Medical Number'}),
        'number_of_passengers' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Number of Passengers - Use digits'}),
        'start_date' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Start Date'}),
        'end_date' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'End Date'}),

        'pickup_address_one' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Pickup Address One'}),
        'destination_address_one' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Destination Address One'}),
        'pickup_time_one' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Pickup Time One'}),
        'return_time_one' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Return Time One'}),
        'weekday_one' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Type first 3 letters of the weekday'}),

        'pickup_address_two' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Pickup Address Two'}),
        'destination_address_two' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Destination Address Two'}),
        'pickup_time_two' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Pickup Time Two'}),
        'return_time_two' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Return Time Two'}),
        'weekday_two' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Type first 3 letters of weekday two'}),

        # 'pickup_time_three' : forms.TextInput(attrs={'class' : 'form-control'}),
        # 'return_time_three' : forms.TextInput(attrs={'class' : 'form-control'}),
        # 'pickup_day_three' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Type first 3 letters of the weekday'}),
        #
        # 'pickup_time_four' : forms.TextInput(attrs={'class' : 'form-control'}),
        # 'return_time_four' : forms.TextInput(attrs={'class' : 'form-control'}),
        # 'pickup_day_four' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Type first 3 letters of the weekday'}),
        #
        # 'pickup_time_five' : forms.TextInput(attrs={'class' : 'form-control'}),
        # 'return_time_five' : forms.TextInput(attrs={'class' : 'form-control'}),
        # 'pickup_day_five' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Type first 3 letters of the weekday'}),
        #
        # 'pickup_time_six' : forms.TextInput(attrs={'class' : 'form-control'}),
        # 'return_time_six' : forms.TextInput(attrs={'class' : 'form-control'}),
        # 'pickup_day_six' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Type first 3 letters of the weekday'}),
        #
        # 'pickup_time_seven' : forms.TextInput(attrs={'class' : 'form-control'}),
        # 'return_time_seven' : forms.TextInput(attrs={'class' : 'form-control'}),
        # 'pickup_day_seven' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Type first 3 letters of the weekday'}),
        }

        # 'pickup_time_three','return_time_three','pickup_day_three','pickup_time_four','return_time_four','pickup_day_four','pickup_time_five','return_time_five','pickup_day_five', 'pickup_time_six','return_time_six','pickup_day_six'
