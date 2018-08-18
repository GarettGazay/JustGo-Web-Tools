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
    DAY_CHOICES = (('Mon','Mon'),('Tue','Tue'),('Wed','Wed'),('Thur','Thur'),('Fri','Fri'),('Sat','Sat'),('Sun','Sun'))

    weekdays = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=DAY_CHOICES,
    )

    class Meta:
        model = models.Reocurring
        fields = ['account_number','call_number','service_type','patient_name', 'patient_phone','patient_birthdate','patient_med_number','number_of_passengers','pickup_address','destination_address','pickup_time','return_time','weekdays','start_date','end_date']

        widgets = {
        'account_number' : forms.TextInput(attrs={'class' : 'form-control'}),
        'call_number' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'SCFHP only'}),
        'service_type' : forms.TextInput(attrs={'class' : 'form-control'}),
        'patient_name' : forms.TextInput(attrs={'class' : 'form-control'}),
        'patient_phone' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'SCFHP  only'}),
        'patient_birthdate' : forms.DateInput(attrs={'class' : 'form-control'}),
        'patient_med_number' : forms.TextInput(attrs={'class' : 'form-control'}),
        'number_of_passengers' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Number of Passengers - Use digits'}),

        'pickup_address' : forms.TextInput(attrs={'class' : 'form-control'}),
        'destination_address' : forms.TextInput(attrs={'class' : 'form-control'}),
        'pickup_time' : forms.TextInput(attrs={'class' : 'form-control'}),
        'return_time' : forms.TextInput(attrs={'class' : 'form-control'}),
        'start_date' : forms.TextInput(attrs={'class' : 'form-control'}),
        'end_date' : forms.TextInput(attrs={'class' : 'form-control'}),
}
