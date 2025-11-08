from django.shortcuts import render
from .models import Beneficiary  

# Create your views here.


def beneficiary_list(request):


    return render(request, 'beneficiaries-list.html',{
        'beneficiaries': Beneficiary
    })

def beneficiary_details(request):

    return render(request,'beneficiaries-details.html')

