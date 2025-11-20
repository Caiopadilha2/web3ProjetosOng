from django.shortcuts import render, get_object_or_404,redirect
from django.http import JsonResponse
from django.contrib import messages
from .models import Donation
from beneficiaries.models import Beneficiary
from stock.models import StockEntry
from datetime import date, datetime
from donations.forms import DonationRegisterForm



def donation_list(request):
    donations = Donation.objects.select_related('beneficiary_fk').all()

    context = {
        'donations' : donations,                                                 
                                                   
    }

    return render(request, 'donations-list.html', context)



def donation_details(request, pk):

    donation = get_object_or_404(Donation.objects.select_related('beneficiary_fk'), pk = pk)

    if request.method == 'POST':
        donation.delete()

        return render(request, 'donations-list.html', {
            'donations': Donation.objects.select_related('beneficiary_fk').all(),
        })
    

    return render(request,'donations-details.html', { 'donation': donation, })



def donation_register(request):
     

    if request.method == 'POST':
        form = DonationRegisterForm(request.POST)
        
        if form.is_valid():
            try:
                created_donations = form.save()
                messages.success(
                    request, 
                    f'{len(created_donations)} doação(ões) criada(s) com sucesso!'
                )
                return redirect('donations:registrar_doaçoẽs') 
            except Exception as err:
                messages.error(request, f'**Erro ao criar doações: {str(err)}')
        
        else:
            messages.error(request, '**Por favor, selecione pelo menos um beneficiário para efetuar a doação.')
    
    
    else:
        form = DonationRegisterForm()


    available_stock_count = StockEntry.objects.filter(
        is_available=True
    ).exclude(
        donation__isnull=False
    ).count()
    
    return render(request, 'register-donations.html', {
        'form': form,
        'available_stock_count': available_stock_count, 
    })


def unique_donation_register(request, pk):
    
    beneficiary = get_object_or_404(Beneficiary, pk = pk)
    stock_entry = stock_entry = StockEntry.objects.filter(
        is_available=True
    ).exclude(
        donation__isnull=False
    ).first()

    available_stock_count = StockEntry.objects.filter(
        is_available=True
    ).exclude(
        donation__isnull=False
    ).count()



    if request.method == 'POST' and available_stock_count > 0 :
        today = date.today()
        now = datetime.now()

        if stock_entry:

            try:

                created_donation = Donation.objects.create(
                        beneficiary_fk=beneficiary,
                        stock_entry_fk=stock_entry,
                        donation_month=str(today.month),
                        donation_year=today.year,
                        description=f" ",
                    )
                
                stock_entry.is_available = False
                stock_entry.exit_date = today
                stock_entry.exit_time = now.time()
                stock_entry.save()

                
                return JsonResponse({
                    'success': True,
                    'message': f'**Doação registrada com sucesso para {beneficiary.beneficiary_name}!'
                })


            except Exception as err:

                return JsonResponse({
                    'success': False,
                    'message': f'**Erro ao criar doação: {str(err)}'
                }, status=400)
                


        else:

            return JsonResponse({                
                'success': False,
                'message': '**Não há cestas disponíveis no momento.'
            }, status=400)


    return JsonResponse({
        'success': False,
        'message': 'Requisição inválida.'
    }, status=400)    


            

        
    



         


