from django.contrib import admin
from projects.models import Project
from projects.models import Enrollment



class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id_project','project_name', 'project_description', 'start_date', 'end_date', 'project_type','created_at')
    search_fields = ('id_project','project_name')




admin.site.register(Project,ProjectAdmin)


class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('id_Enrollment','beneficiary_fk', 'project_fk', 'enrollment_stamp')
    search_fields = ('id_Enrollment','beneficiary_fk','project_fk')




admin.site.register(Enrollment,EnrollmentAdmin)



# Register your models here.
