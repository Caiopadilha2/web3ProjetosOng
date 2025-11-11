from django.shortcuts import render, get_object_or_404
from .models import Beneficiary  

# Create your views here.


def beneficiary_list(request):

    beneficiaries = Beneficiary.objects.all()




    return render(request, 'beneficiaries-list.html',{
        'beneficiaries': beneficiaries
    })

def beneficiary_details(request,pk):
    beneficiary = get_object_or_404(Beneficiary,pk = pk )

    return render(request,'beneficiaries-details.html',{'beneficiary': beneficiary})



def beneficiary_form(request):
    return render(request,'registration-form.html' )


def beneficiary_autoform(request):
    return render(request, 'auto-registration-form.html')
