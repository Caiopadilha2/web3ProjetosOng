from django.urls import path
from .views import supplier_list, supplier_details, stock_entry,supplier_form,supplier_edit, stock_entry_form,supplier_delete


app_name = 'stock'


urlpatterns = [
 


    path('suppliers/list/',supplier_list, name='fornecedores'),
    path('suppliers/<int:pk>/',supplier_details, name='detalhes_fornecedores'),   
    path('suppliers/register/',supplier_form, name='form_fornecedor'),
    path('suppliers/<int:pk>/edit/',supplier_edit, name='editar_fornecedor'),
    path('suppliers/delete/<int:pk>/',supplier_delete,name='deletar_Fornecedores'),      
    path('entries/append/<int:stock_id>/',stock_entry, name='aplicar_entradas'),
    path('entries/', stock_entry_form, name='entradas'),
    
]
