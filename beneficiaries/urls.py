from django.urls import path
from beneficiaries.views import beneficiary_list, beneficiary_details, beneficiary_form, beneficiary_autoform



app_name = 'beneficiaries'

urlpatterns = [
    path('',beneficiary_list, name='Beneficiarios'),
    path('<int:pk>/',beneficiary_details, name='detalhes_beneficiarios'),
    path('register/', beneficiary_form, name='form_beneficiarios'),
    path('autoregister/', beneficiary_autoform, name='autoform_beneficiarios'),


   

]

