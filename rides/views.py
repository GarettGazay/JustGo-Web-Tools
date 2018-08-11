from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from .models import FormBasic, Reoccuring

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
    one_off = FormBasic.objects.all().order_by('time_stamp')
    reocurring = Reoccuring.objects.all().order_by('time_stamp')
    return render(request, 'rides/download.html', {'one_off' : one_off, 'reoccuring' : reocurring})
