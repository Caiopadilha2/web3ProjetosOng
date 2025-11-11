from django.urls import path
from .views import supplier_list, supplier_details, stock_entry




app_name = 'stock'


urlpatterns = [
    path('list/',supplier_list, name='Fornecedores'),
    path('<int:pk>/',supplier_details,name='detalhes_Fornecedores'),   
    path('append/',stock_entry, name='entradas'),   

]
