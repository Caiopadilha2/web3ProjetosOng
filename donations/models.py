from django.db import models

MONTH_CHOICES = [
    ('1' , 'Janeiro' ),
    ('2' , 'Fevereiro' ),
    ('3' , 'Março' ),
    ('4' , 'Abril' ),
    ('5' , 'Maio' ),
    ('6' , 'Junho' ),
    ('7' , 'Julho' ),
    ('8' , 'Agosto' ),
    ('9' , 'Setembro' ),
    ('10', 'Outubro' ),
    ('11', 'Novembro' ),
    ('12' , 'Dezembro' ),

]


class Donation(models.Model):

    id_donation = models.AutoField(primary_key=True)
    beneficiary_fk = models.ForeignKey('beneficiaries.Beneficiary',on_delete=models.CASCADE,verbose_name="Beneficiário")
    stock_entry_fk = models.OneToOneField('stock.StockEntry', on_delete=models.PROTECT,verbose_name="Entrada de Estoque")
    description = models.CharField(max_length=200, blank= True, null= True, verbose_name="Descrição")
    donation_date = models.DateField(auto_now_add= True, verbose_name="Data da Doação")
    donation_time = models.TimeField(auto_now_add= True, verbose_name="Hora da Doação")
    donation_month = models.CharField(max_length= 2, choices = MONTH_CHOICES, verbose_name="Mês da Doação")
    donation_year = models.IntegerField(verbose_name="Ano da Doação")

    def __str__(self):
        return str(self.id_donation)
    


    class Meta:
        unique_together = ['beneficiary_fk', 'donation_month', 'donation_year']
        verbose_name = 'Doação'
        verbose_name_plural = 'Doações'

