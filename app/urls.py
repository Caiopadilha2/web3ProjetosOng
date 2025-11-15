from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('beneficiaries/',include('beneficiaries.urls')),
    
    path('donations/',include('donations.urls')),    
    path('projects/', include('projects.urls')),
    path('stock/suppliers/', include('stock.urls' , namespace='sotck_suppliers')),
    path('stock/entries/', include('stock.urls', namespace='stock_entries')),


    path('',RedirectView.as_view(url='accounts/login/')),


   
]
