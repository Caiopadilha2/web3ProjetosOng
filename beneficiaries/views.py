from django.shortcuts import render, get_object_or_404,redirect
from .models import Beneficiary  
from beneficiaries.forms import BeneficiariesModelForm,auto_register_Form

# Create your views here.


def beneficiary_list(request):

    beneficiaries = Beneficiary.objects.all()




    return render(request, 'beneficiaries-list.html',{
        'beneficiaries': beneficiaries
    })

def beneficiary_details(request,pk):

    beneficiary = get_object_or_404(Beneficiary,pk = pk )

    if request.method == 'POST':
        beneficiary.delete()
        # return render(request, 'beneficiaries-list.html', {
        #     'beneficiaries': Beneficiary.objects.all()
        # })
        return redirect('form_beneficiarios')

    return render(request,'beneficiaries-details.html',{'beneficiary': beneficiary})



def beneficiary_form(request):
    success = False 

    if request.method == 'POST':
        form = BeneficiariesModelForm(request.POST)
        if form.is_valid():
            form.save()
            success = True  
            form = BeneficiariesModelForm()
    else:
        form = BeneficiariesModelForm()

    return render(request, 'registration-form.html', {'form': form, 'success': success})




def beneficiary_autoform(request):
    success = False 

    if request.method == 'POST':
        form = auto_register_Form(request.POST)
        if form.is_valid():
            form.save()
            success = True  
            form = auto_register_Form()
    else:
        form = auto_register_Form()

    return render(request, 'auto-registration-form.html', {'form': form, 'success': success})
    
