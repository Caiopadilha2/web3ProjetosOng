from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
from projects.forms import ProjectForm


# Create your views here.

def project_list(request):
    projects = Project.objects.all() 

    success = False 

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            success = True  
            form = ProjectForm()
            return redirect('/projects/')
    else:
        form = ProjectForm()

        context = {
        'form': form,
        'success': success,
        'projects': projects
    }

    return render(request, 'projects.html', context)


def project_details(request, pk):
    project = get_object_or_404(Project, pk = pk)
    enrollments = project.enrollment_set.select_related('beneficiary_fk').all().order_by('beneficiary_fk__beneficiary_name')

    if request.method == 'POST':
        project.delete()
        return render(request, 'projects.html', {
            'projects': Project.objects.all()
        })
    
    context = {
        'project' : project,
        'enrollments' : enrollments,
        
    }

    return render(request,'projects-details.html', context )

def project_edit(request,pk):
    project = get_object_or_404(Project, pk=pk)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid:
            form.save()
            return redirect('projects:Projetos')
    else:
        form = ProjectForm(instance=project)
    
    return render(request,'projects-edit.html',{'form': form, 'project': project})





