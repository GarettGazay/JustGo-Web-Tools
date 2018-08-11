from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from .models import FormBasic, Reoccuring
import csv

# Create your views here.

@login_required(login_url='/accounts/login')
def book_view(request):
    if request.method == 'POST':
        form = forms.CreateBooking(request.POST,request.FILES)
        print(form.errors)
        if form.is_valid():
            #save booking to DB
            instance = form.save(commit=False)
            instance.author= request.user
            instance.save()
            return redirect('rides:book') # Make a congratulations app
        else:
            return redirect('rides:book')
    else:
        form = forms.CreateBooking()
        return render(request, 'rides/form.html',{'form': form})


@login_required(login_url='/accounts/login')
def book_view_reoccuring(request):
    if request.method == 'POST':
        form = forms.ReoccuringBooking(request.POST,request.FILES)
        print(form.errors)
        if form.is_valid():
            #save booking to DB
            instance = form.save(commit=False)
            instance.author= request.user
            instance.save()
            return redirect('rides:multi') # Make a congratulations url
        else:
            return redirect('rides:multi')
    else:
        form = forms.ReoccuringBooking()
        return render(request, 'rides/reoccuring.html',{'form': form})

@login_required(login_url='/accounts/login')
def download_page(request):
    one_off = FormBasic.objects.all().order_by('-time_stamp')
    reocurring = Reoccuring.objects.all().order_by('-time_stamp')
    return render(request, 'rides/download.html', {'one_off' : one_off, 'reoccuring' : reocurring})

@login_required(login_url='/accounts/login')
def one_off_dr(request, pk=None):
    if pk:
        print('returned private key: ',pk)
        db = FormBasic.objects.get(pk=pk)
        name = db.patient_name
        phone = db.patient_phone
        start_address = db.pickup_address
        end_address = db.destination_address
        pickup_date = (db.appointment_date + ' ' + db.pickup_time)
        return_date = ''
        account_id = db.account_number
        service_type = db.service_type
        passengers = db.number_of_passengers
        customer_notes = ''
        driver_name = ''
        driver_notes = ''
        dispatcher_notes = db.call_number
        driver_email = ''

        # Create CSV
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="dashride-upload.csv"'

        writer = csv.writer(response)
        writer.writerow(['customer_name','customer_phone','customer_email','start_address','end_address','pickup_date','return_date','account_id','service_type','passengers','driver_notes','customer_notes','driver_name','driver_email'])
        writer.writerow([name,phone,'', start_address, end_address, pickup_date, return_date, account_id, service_type,passengers,driver_notes,dispatcher_notes,customer_notes,driver_name,driver_email])
        return response

    else:
        print('Something went wrong')
        one_off = FormBasic.objects.all().order_by('-time_stamp')
        reocurring = Reoccuring.objects.all().order_by('-time_stamp')
        return render(request, 'rides/download.html', {'one_off' : one_off, 'reoccuring' : reocurring})
