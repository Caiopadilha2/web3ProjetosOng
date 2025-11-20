from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Supplier,StockEntry, Stock
from stock.form import suppliers_form, StockEntryForm


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
        
        redirect('stock:fornecedores')



def stock_entry_form(request):
    available_stock_count = StockEntry.objects.filter(
        is_available=True
    ).exclude(
        donation__isnull=False
    ).count()
    stock = Stock.objects.get(pk=1)

    form = StockEntryForm(stock=stock)
    
    stocks = Stock.objects.all()
    return render(request, 'stock-entry.html', {'available_stock_count': available_stock_count,'form':form,'stocks': stocks})



def stock_entry(request,stock_id):
                
    stock = Stock.objects.get(pk=stock_id)
    
    if request.method == 'POST':
        form = StockEntryForm(request.POST, stock=stock)
        
        if form.is_valid():
            supplier = form.cleaned_data['supplier_fk']
            quantity = form.cleaned_data['quantity']
            
            # Gera o próximo número de lote automaticamente
            last_entry = StockEntry.objects.order_by('-batch').first()
            next_batch = (last_entry.batch + 1) if last_entry else 1
            
            # Cria as entradas em lote
            entries = []
            for i in range(quantity):
                entry = StockEntry(
                    stock_fk=stock,
                    supplier_fk=supplier,
                    batch=next_batch
                )
                entries.append(entry)
            
            # Salva tods de uma vezz 
            StockEntry.objects.bulk_create(entries)
            
            messages.success(request, f'{quantity} entrada(s) registrada(s) com sucesso no lote #{next_batch}!')
            return redirect('stock:entradas')
    else:
        form = StockEntryForm(stock=stock)
    
    return render(request, 'stock-entry.html', {'form': form, 'stock': stock})









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
    


