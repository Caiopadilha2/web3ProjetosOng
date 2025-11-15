from django.shortcuts import render, get_object_or_404,redirect
from .models import Beneficiary
from projects.models import Enrollment     
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




def beneficiary_delete(request, pk):
    beneficiary = get_object_or_404(Beneficiary,pk = pk)

    if request.method == 'POST':
        beneficiary.delete()

        redirect('Beneficiarios')










def beneficiary_form(request):
    success = False 

    if request.method == 'POST':
        form = BeneficiariesModelForm(request.POST)
        if form.is_valid():

            beneficiario = form.save(commit=False)
            beneficiario.save()

            projeto = form.cleaned_data['projeto']
            Enrollment.objects.create(
                beneficiary_fk = beneficiario,
                project_fk = projeto

            ) 

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
            
            beneficiario = form.save(commit=False)
            beneficiario.save()

            projeto = form.cleaned_data['projeto']
            Enrollment.objects.create(
                beneficiary_fk = beneficiario,
                project_fk = projeto

            ) 
            success = True  
            form = auto_register_Form()
    else:
        form = auto_register_Form()

    return render(request, 'auto-registration-form.html', {'form': form, 'success': success})


def beneficiary_edit(request, pk):
    beneficiary = get_object_or_404(Beneficiary, pk=pk)

    if request.method == 'POST':
        form = BeneficiariesModelForm(request.POST, instance=beneficiary)
        if form.is_valid():
            form.save()
            return redirect('beneficiaries:Beneficiarios') 
    else:
        form = BeneficiariesModelForm(instance=beneficiary)

    return render(request, 'edit-form.html', {'form': form, 'beneficiary': beneficiary})
    
