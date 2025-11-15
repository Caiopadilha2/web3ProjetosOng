from django.db import models



class Supplier(models.Model):
    TYPE_CHOICE = [
    ('PJ', 'Pessoa Jurídica'),
    ('PF', 'Pessoa Física')
    ]

    UF_CHOICE = [
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
    ('TO', 'Tocantins')
    ]




    id_supplier = models.AutoField(primary_key=True)
    supplier_name = models.CharField(max_length=50, blank=True,null=True, verbose_name="Nome do Doador")
    supplier_type = models.CharField(max_length=2,choices=TYPE_CHOICE, blank=False,null=False, verbose_name="Tipo de doador")
    tax_id = models.CharField(max_length=18,unique=True, blank=False,null=False, verbose_name="CPF/CNPJ")
    zip_code = models.CharField(max_length=9, blank=True, null=True, verbose_name="CEP")
    street = models.CharField(max_length=200, blank=True, null=True, verbose_name="Rua")
    address_number = models.CharField(max_length=10, blank=True, null=True, verbose_name="Número")
    address_complement = models.CharField(max_length=50, blank=True,null=True,verbose_name="Complemento")
    neighborhood = models.CharField(max_length=100,blank=True,null=True,verbose_name="Bairro")
    city = models.CharField(max_length=100,blank=False,null=False,verbose_name="Cidade")
    state = models.CharField(max_length=2, choices=UF_CHOICE,blank=False, null=False,verbose_name="UF")
    phone = models.CharField(max_length=15,blank=False,null=False,verbose_name="Telefone")
    email = models.EmailField(blank=False,null=False,verbose_name="E-mail")
    is_anonymous = models.BooleanField(default=False)

    


    def __str__(self):
        return self.supplier_name
    
    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'
    




class Stock(models.Model):
    id_stock = models.AutoField(primary_key=True)
    stock_name = models.CharField(max_length=100, blank=False,null=False, verbose_name="Nome")
    stock_description = models.CharField(max_length=200, blank=False, null=False, verbose_name="Descrição")
    quantity =models.IntegerField(blank=False,null=False,default=0, verbose_name="Quantidade")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Ultima atualização")
    
    suppliers = models.ManyToManyField('Supplier', through='StockEntry')


    def __str__(self):
        return self.stock_name
    
    class Meta:
        verbose_name = 'Estoque'
        verbose_name_plural = 'Estoque'

    




class StockEntry(models.Model):
    id_stockentry = models.AutoField(primary_key=True)
    stock_fk = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='entries', verbose_name="Estoque")
    supplier_fk = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Fornecedor")
    batch = models.IntegerField(blank=False,null=False, verbose_name="Lote")
    entry_date = models.DateField(auto_now_add=True, verbose_name="Data da Entrada")
    entry_time = models.TimeField(auto_now_add=True, verbose_name="Hora da Entrada")

    exit_date = models.DateField(blank=True, null=True, verbose_name="Data de Saída")
    exit_time = models.TimeField(blank=True, null=True, verbose_name="Hora de Saída")
    is_available = models.BooleanField(default=True, verbose_name="Disponibilidade")


    def __str__(self):
        return str(self.id_stockentry)
    

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'







    
