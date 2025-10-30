from django.db import models


TYPE_CHOICES = [
        ('course', 'Curso'),
        ('Meeting', 'Encontro'),
        ('Lecture', 'Palestra'),
    ]



class Project(models.Model):
    id_project = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=50, blank=False,null=False, verbose_name="Nome Projeto")
    project_description = models.CharField(max_length=200, blank=True, null=True, verbose_name="Descrição")
    start_date = models.DateField(blank=False,null=False,verbose_name="Data de Início")
    end_date = models.DateField(blank=True,null=True,verbose_name="Data do fim")
    project_type = models.CharField(max_length=20, choices=TYPE_CHOICES, verbose_name="Tipo")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data do Registro")


    def __str__(self):
        return self().project_name



class Enrollment(models.Model):

    id_Enrollment = models.AutoField(primary_key=True)
    beneficiary_fk = models.ForeignKey('beneficiaries.Beneficiary',on_delete=models.CASCADE,verbose_name="Beneficiário")
    project_fk = models.ForeignKey('Project', on_delete=models.CASCADE, verbose_name="Projeto")
    enrollment_stamp = models.DateTimeField(auto_now_add=True, verbose_name="Data/Hora da Inscrição")
    
    
      
    
    def __str__(self):
        return self().model
    

    class Meta:
        unique_together = ['beneficiary_fk', 'project_fk']