from django import forms
from . import models
from django.http import HttpResponse

class CreateBooking(forms.ModelForm):
    GENDER_CHOICES = (('Male', 'Male'),('Female', 'Female'))
    SERVICE_TYPES = (('SCFHP Basic','SCFHP Basic'),('VMC Wheelchair','VMC Wheelchair'),('VMC Ambulatory','VMC Ambulatory'),('VMC Discharge','VMC Discharge'))
    ACCOUNT_NUMBERS = (('SC00001','SC00001'),('Fatima001','Fatima001'),('OLISCC','OLISCC'),('KINSCC','KINSCC'),('VICSCC','VICSCC'),('MCDSCC','MCDSCC'))

    account_number = forms.ChoiceField(required=True,choices=ACCOUNT_NUMBERS)
    service_type = forms.ChoiceField(required=True,choices=SERVICE_TYPES)

    class Meta:
        model = models.FormBasic
        fields = ['account_number','service_type','call_number','patient_med_number','patient_first_name','patient_last_name','gender', 'patient_phone','patient_birthdate','number_of_passengers','appointment_date', 'pickup_time','return_time', 'pickup_address', 'destination_address','round_trip',]
        widgets = {
        'call_number'  : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'SCFHP Only'}),
        'patient_first_name' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Patient First Name'}),
        'patient_last_name' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Patient Last Name'}),
        'patient_phone' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder': '10-Digit - Digits Only'}),
        'patient_birthdate' : forms.DateInput(attrs={'class' : 'form-control', 'placeholder' : 'MMDDYYYY'}),
        'patient_med_number' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'SCFHP Only'}),
        'number_of_passengers' : forms.NumberInput(attrs={'class' : 'form-control'}),
        'appointment_date' : forms.TextInput(attrs={'class' : 'form-control'}),
        'pickup_time' : forms.TextInput(attrs={'class' : 'form-control'}),
        'return_time' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Leave blank if one way'}),
        'pickup_address' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Example: 220 University Ave, Palo Alto, CA 94301'}),
        'destination_address' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Example: 220 University Ave, Palo Alto, CA 94301'}),
        'round_trip' : forms.CheckboxInput(attrs={'style' : 'margin: 0 auto; width: 30px; height: 30px;'}),
        }


class ReocurringBooking(forms.ModelForm):
    DAY_CHOICES = (('Mon','Mon'),('Tue','Tue'),('Wed','Wed'),('Thur','Thur'),('Fri','Fri'),('Sat','Sat'),('Sun','Sun'))
    GENDER_CHOICES = (('Male', 'Male'),('Female', 'Female'))
    SERVICE_TYPES = (('SCFHP Basic','SCFHP Basic'),('VMC Wheelchair','VMC Wheelchair'),('VMC Ambulatory','VMC Ambulatory'),('VMC Discharge','VMC Discharge'))
    ACCOUNT_NUMBERS = (('SC00001','SC00001'),('Fatima001','Fatima001'),('OLISCC','OLISCC'),('KINSCC','KINSCC'),('VICSCC','VICSCC'),('MCDSCC','MCDSCC'))

    weekdays = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=DAY_CHOICES,
    )

    gender = forms.ChoiceField(required=True,choices=GENDER_CHOICES)

    class Meta:
        model = models.Reocurring
        fields = ['account_number','service_type','call_number','patient_first_name', 'patient_last_name','gender', 'patient_phone','patient_birthdate','patient_med_number','number_of_passengers','pickup_address','destination_address','pickup_time','return_time','start_date','end_date','weekdays','round_trip',]

        widgets = {
        'call_number' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'SCFHP only'}),
        'patient_first_name' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Patient First Name'}),
        'patient_last_name' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Patient Last Name'}),
        'patient_phone' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : '10-Digit - Digits Only'}),
        'patient_birthdate' : forms.DateInput(attrs={'class' : 'form-control','placeholder' : 'MMDDYYYY'}),
        'patient_med_number' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'SCFHP Only'}),
        'number_of_passengers' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Number of Passengers - Use digits'}),
        'pickup_address' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Example: 220 University Ave, Palo Alto, CA 94301'}),
        'destination_address' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Example: 220 University Ave, Palo Alto, CA 94301'}),
        'pickup_time' : forms.TextInput(attrs={'class' : 'form-control'}),
        'return_time' : forms.TextInput(attrs={'class' : 'form-control'}),
        'start_date' : forms.TextInput(attrs={'class' : 'form-control'}),
        'end_date' : forms.TextInput(attrs={'class' : 'form-control'}),
        'round_trip' : forms.CheckboxInput(attrs={'style' : 'margin: 0 auto; width: 30px; height: 30px;'}),

}
