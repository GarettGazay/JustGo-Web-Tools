from django.shortcuts import render

# Create your views here.

def data_formatter(request):
    return render(request, 'data_format/data_format.html')
