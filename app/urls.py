from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('beneficiaries/',include('beneficiaries.urls')),
    path('donations/',include('donations.urls')),
    path('suppliers/', include('stock.urls', namespace='suppliers') ),
    path('projects/', include('projects.urls')),
    path('stock', include('stock.urls', namespace='stock')),


    path('',RedirectView.as_view(url='accounts/login/')),


   
]
