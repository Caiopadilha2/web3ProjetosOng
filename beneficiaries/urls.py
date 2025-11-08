from django.urls import path
from beneficiaries.views import beneficiary_list, beneficiary_details



app_name = 'beneficiaries'

urlpatterns = [
    path('',beneficiary_list, name='Beneficiarios'),
    path('details/',beneficiary_details, name='Detalhes_beneficiarios'),

   

]

