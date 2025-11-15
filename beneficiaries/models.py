from django.db import models

# Create your models here.

class Beneficiary(models.Model):
    STATUS_CHOICES = [
        ('active', 'Ativo'),
        ('pending', 'Pendente'),
        ('suspended', 'Suspenso'),
    ]
    UF_CHOICES = [
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AM', 'Amazonas'),
    ('AP', 'Amapá'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('PR', 'Paraná'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SE', 'Sergipe'),
    ('SP', 'São Paulo'),
    ('TO', 'Tocantins'),
]

    id_beneficiary = models.AutoField(primary_key=True)
    beneficiary_name = models.CharField(max_length=200,verbose_name="Nome Completo")
    birth_date = models.DateField(verbose_name="Data de nascimento")
    cpf = models.CharField(max_length=14,unique=True, blank=False, null=False,)
    zip_code = models.CharField(max_length=9,blank=False,null=False,verbose_name="CEP")
    street = models.CharField(max_length=200, blank=False, null=False, verbose_name="Rua")
    address_number = models.IntegerField(blank=False,null=False,verbose_name="Número") 
    address_complement = models.CharField(max_length=50, blank=True,null=True,verbose_name="Complemento")
    neighborhood = models.CharField(max_length=100,blank=False,null=False,verbose_name="Bairro")
    city = models.CharField(max_length=100,blank=False,null=False,verbose_name="Cidade")
    state = models.CharField(max_length=2, choices=UF_CHOICES,blank=False, null=False,verbose_name="UF")
    phone = models.CharField(max_length=15,blank=False,null=False,verbose_name="Telefone")
    email = models.EmailField(blank=False,null=False,verbose_name="E-mail")
    occupation = models.CharField(max_length=100, verbose_name="Profissão")
    family_income = models.DecimalField(max_digits=10,decimal_places=2, verbose_name="Renda Familiar")
    dependents_count = models.IntegerField(default=0,blank=True,null=True, verbose_name="Nº dependentes")
    household_members = models.IntegerField(blank=False,null=False,verbose_name="Nº de pessoas da Família")
    status = models.CharField(max_length=10,choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data do Registro")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Ultima atualização")

    projects = models.ManyToManyField('projects.Project', through='projects.Enrollment')

    def __str__(self):
        return self.beneficiary_name
    
    class Meta:
        verbose_name = 'Beneficiário'
        verbose_name_plural = 'Beneficiários'