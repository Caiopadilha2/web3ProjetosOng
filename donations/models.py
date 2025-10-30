from django.db import models



class Donation(models.Model):

    id_donation = models.AutoField(primary_key=True)
    beneficiary_fk = models.ForeignKey('beneficiaries.Beneficiary',on_delete=models.CASCADE,verbose_name="Beneficiário")
    stock_entry_fk = models.OneToOneField('stock.StockEntry', on_delete=models.PROTECT,verbose_name="Entrada de Estoque")
    description = models.CharField(max_length=200, blank=False, null=False, verbose_name="Descrição")
    donation_date = models.DateField(auto_now_add=True, verbose_name="Data da Doação")
    donation_time = models.TimeField(auto_now_add=True, verbose_name="Hora da Doação")
    donation_month = models.IntegerField(verbose_name="Mês da Doação")
    donation_year = models.IntegerField(verbose_name="Ano da Doação")

    def __str__(self):
        return self().id_donation
    


    class Meta:
        unique_together = ['beneficiary_fk', 'donation_month', 'donation_year']

