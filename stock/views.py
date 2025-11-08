from django.shortcuts import render
from .models import Supplier


def supplier_list (request):
    return render(request, 'suppliers-list.html')



def supplier_details(request):
    return render(request, 'suppliers-details.html')


def stock_entry(request):
    return render(request,'stock-entry.html')


