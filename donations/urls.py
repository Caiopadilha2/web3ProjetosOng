from django.urls import path
from donations.views import donation_list, donation_details



app_name = 'donations'

urlpatterns = [
    path('', donation_list, name='Doação'),
    path('<int:pk>/', donation_details, name='Detalhes doação'),

   

]


