from django.shortcuts import render, get_object_or_404, redirect
from .models import Supplier
from stock.form import suppliers_form


def supplier_list (request):
    suppliers = Supplier.objects.all()

    return render(request, 'suppliers-list.html', {'suppliers' : suppliers} )



def supplier_details(request, pk):

    supplier = get_object_or_404(Supplier, pk = pk)

    return render(request, 'suppliers-details.html', { 'supplier': supplier })



def supplier_delete(request, pk):
    supplier = get_object_or_404(Supplier,pk = pk)

    if request.method == 'POST':
        supplier.delete()
        
        redirect('Fornecedores')




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

def supplier_edit(request,pk):
    supplier = get_object_or_404(Supplier, pk=pk)

    if request.method == 'POST':
        form = suppliers_form(request.POST, instance=supplier)
        if form.is_valid:
            form.save()
            return redirect('stock:Fornecedores')
    else:
        form = suppliers_form(instance=supplier)
    
    return render(request,'suppliers-edit.html',{'form': form, 'supplier': supplier})
    


