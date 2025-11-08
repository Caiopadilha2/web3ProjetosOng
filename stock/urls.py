from django.urls import path
from .views import supplier_list, supplier_details, stock_entry




app_name = 'stock'


urlpatterns = [
    path('suppliers',supplier_list, name='Fornecedores'),
    path('details/',supplier_details, name='Detalhes_Fornecedores'),   
    path('',stock_entry, name='Estoque'),   

]
