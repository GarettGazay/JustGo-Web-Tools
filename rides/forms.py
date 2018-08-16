from django import forms
from . import models
from django.http import HttpResponse

class CreateBooking(forms.ModelForm):

    class Meta:
        model = models.FormBasic
        fields = ['account_number','call_number','service_type','patient_name', 'patient_phone','patient_birthdate','patient_med_number','number_of_passengers','appointment_date', 'pickup_time','return_time', 'pickup_address', 'destination_address','round_trip',]
        widgets = {
        'account_number' : forms.TextInput(attrs={'class' : 'form-control'}),
        'call_number'  : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'SCFHP only'}),
        'service_type'  : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'SCFHP only'}),
        'patient_name' : forms.TextInput(attrs={'class' : 'form-control'}),
        'patient_phone' : forms.TextInput(attrs={'class' : 'form-control'}),
        'patient_birthdate' : forms.DateInput(attrs={'class' : 'form-control', 'placeholder' : 'This field SCFHP only'}),
        'patient_med_number' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'This field SCFHP only'}),
        'number_of_passengers' : forms.NumberInput(attrs={'class' : 'form-control'}),
        'appointment_date' : forms.TextInput(attrs={'class' : 'form-control'}),
        'pickup_time' : forms.TextInput(attrs={'class' : 'form-control'}),
        'return_time' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Leave blank if one way'}),
        'pickup_address' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Address + City + State + Zip'}),
        'destination_address' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Address + City + State + Zip'}),
        'round_trip' : forms.CheckboxInput(attrs={'style' : 'margin: 0 auto; width: 30px; height: 30px;'}),

        }


class ReocurringBooking(forms.ModelForm):

    class Meta:
        model = models.Reocurring
        fields = ['patient_name', 'patient_phone','patient_birthdate','patient_med_number','number_of_passengers','month','pickup_address_one','destination_address_one','pickup_time_one','return_time_one','weekday_one', 'pickup_address_two','destination_address_two','pickup_time_two','return_time_two','weekday_two','pickup_address_three','destination_address_three','pickup_time_three','return_time_three','weekday_three','pickup_address_four','destination_address_four','pickup_time_four','return_time_four','weekday_four','pickup_address_five','destination_address_five','pickup_time_five','return_time_five','weekday_five' ]

        widgets = {
        'patient_name' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Patient Name'}),
        'patient_phone' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Patient Phone Number'}),
        'patient_birthdate' : forms.DateInput(attrs={'class' : 'form-control', 'placeholder' : 'Patient Birthdate'}),
        'patient_med_number' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Patient Medical Number'}),
        'number_of_passengers' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Number of Passengers - Use digits'}),
        'month' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Select Month'}),

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

        'pickup_address_three' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Pickup Address Three'}),
        'destination_address_three' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Destination Address Three'}),
        'pickup_time_three' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Pickup Time Three'}),
        'return_time_three' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Return Time Three'}),
        'weekday_three' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Type first 3 letters of weekday three'}),

        'pickup_address_four' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Pickup Address Four'}),
        'destination_address_four' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Destination Address Four'}),
        'pickup_time_four' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Pickup Time Four'}),
        'return_time_four' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Return Time Four'}),
        'weekday_four' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Type first 3 letters of weekday four'}),

        'pickup_address_five' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Pickup Address Five'}),
        'destination_address_five' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Destination Address Five'}),
        'pickup_time_five' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Pickup Time Five'}),
        'return_time_five' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Return Time Five'}),
        'weekday_five' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Type first 3 letters of weekday five'}),
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
