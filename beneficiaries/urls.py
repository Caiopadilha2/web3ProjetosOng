from django.urls import path


from beneficiaries.views import beneficiary_list, beneficiary_details, beneficiary_form, beneficiary_autoform,beneficiary_edit


#  NÃO APAGAR FIX PARA: BRUNO 
# from beneficiaries.views import beneficiary_list, beneficiary_details,beneficiary_delete, beneficiary_form, beneficiary_autoform




app_name = 'beneficiaries'

urlpatterns = [
    path('list/',beneficiary_list, name='Beneficiarios'),
    path('<int:pk>/',beneficiary_details, name='detalhes_beneficiarios'),
    #  NÃO APAGAR FIX PARA: BRUNO 
    # path('delete/<int:pk>/',beneficiary_delete, name='deletar_beneficiarios'),
    path('register/', beneficiary_form, name='form_beneficiarios'),
    path('autoregister/', beneficiary_autoform, name='autoform_beneficiarios'),
    path('<int:pk>/edit/', beneficiary_edit, name='editar_beneficiario'),
    


   

]

