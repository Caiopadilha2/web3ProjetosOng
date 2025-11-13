from django.shortcuts import render, get_object_or_404
from .models import Supplier
from stock.form import suppliers_form


def supplier_list (request):
    suppliers = Supplier.objects.all()

    return render(request, 'suppliers-list.html', {'suppliers' : suppliers} )



def supplier_details(request, pk):

    supplier = get_object_or_404(Supplier, pk = pk)

    if request.method == 'POST':
        supplier.delete()
        return render(request, 'suppliers-list.html', {
            'suppliers': Supplier.objects.all()
        })

    return render(request, 'suppliers-details.html', { 'supplier': supplier })


def stock_entry(request):
    return render(request,'stock-entry.html')

def supplier_form(request):
    success = False 

    if request.method == 'POST':
        form = suppliers_form(request.POST)
        if form.is_valid():
            form.save()
            success = True  
            form = suppliers_form()
    else:
        form = suppliers_form()

    return render(request, 'suppliers-registration.html', {'form': form, 'success': success})
    


