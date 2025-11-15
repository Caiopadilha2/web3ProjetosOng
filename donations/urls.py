from django.urls import path
from donations.views import donation_list, donation_details

# donation_register

app_name = 'donations'

urlpatterns = [
    path('', donation_list, name='Doação'),
    path('<int:pk>/', donation_details, name='detalhes_doação'),
    # path('register/', donation_register, name='registrar_doaçoẽs')

   

]


