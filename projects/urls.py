from django.urls import path
from projects.views import project_list, project_details,project_edit



app_name = 'projects'


urlpatterns = [
    path('',project_list, name='Projetos'),
    path('<int:pk>/',project_details, name='detalhes_projetos'),
    path('<int:pk>/edit/',project_edit, name='editar_projetos'),

    
    

]