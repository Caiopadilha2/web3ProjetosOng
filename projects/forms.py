from django import forms
from django.core.exceptions import ValidationError
import re
from projects.models import Project

class ProjectForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ("project_name","project_description","start_date","end_date","project_type",)
        widgets = {
            'project_name': forms.TextInput(attrs={
                'class': 'w-full bg-pjr border border-border-light text-foreground-light placeholder-muted-light rounded h-10 px-3 text-sm focus:outline-none focus:ring-2 focus:ring-blue-button/50',
                'id': 'project-name',
                'placeholder': 'Projeto Exemplo'
            }),
            'project_description': forms.Textarea(attrs={
                'class': 'bg-pjr w-full bg-accent-light border border-border-light text-foreground-light placeholder-muted-light rounded p-3 text-sm resize-none focus:outline-none focus:ring-2 focus:ring-blue-button/50',
                'id': 'description',
                'placeholder': 'Uma breve descrição do projeto',
                'rows': '3'
            }),
            'start_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-full bg-pjr border border-border-light text-foreground-light rounded h-10 px-3 text-sm focus:outline-none focus:ring-2 focus:ring-blue-button/50',
                'id': 'start-date'
            }),
            'end_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-full bg-pjr border border-border-light text-foreground-light rounded h-10 px-3 text-sm focus:outline-none focus:ring-2 focus:ring-blue-button/50',
                'id': 'end-date'
            }),
            'project_type': forms.Select(attrs={
                'class': 'w-full bg-pjr border border-border-light text-foreground-light rounded h-10 px-3 text-sm focus:outline-none focus:ring-2 focus:ring-blue-button/50 appearance-none bg-no-repeat bg-right pr-8',
                'id': 'project-type',
                'style': "background-image: url('data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 16 16%27 fill=%27%239cb3bf%27%3e%3cpath fill-rule=%27evenodd%27 d=%27M4.22 6.22a.75.75 0 0 1 1.06 0L8 8.94l2.72-2.72a.75.75 0 1 1 1.06 1.06l-3.25 3.25a.75.75 0 0 1-1.06 0L4.22 7.28a.75.75 0 0 1 0-1.06z%27 clip-rule=%27evenodd%27 /%3e%3c/svg%3e');"
            })

        }
