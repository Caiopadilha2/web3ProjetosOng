from django.shortcuts import render, get_object_or_404
from .models import Donation



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
            'donations': Donation.objects.select_related('beneficiary_fk').all()
        })
    

    return render(request,'donations-details.html', { 'donation': donation })

