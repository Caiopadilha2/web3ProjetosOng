from django.urls import path
from projects.views import project_list, project_details



app_name = 'projects'


urlpatterns = [
    path('',project_list, name='Projetos'),
    path('<int:pk>/',project_details, name='detalhes_projetos'),
    
    

]