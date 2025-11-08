from django.shortcuts import render
from .models import Donation



def donation_list(request):


    return render(request, 'donations-list.html')

def donation_details(request):

    return render(request,'donations-details.html')

