from django.contrib import admin
from beneficiaries.models import Beneficiary

# Register your models here.

class BeneficiaryAdmin(admin.ModelAdmin):
    list_display = ('id_beneficiary','beneficiary_name', 'birth_date', 'cpf', 'zip_code', 'street','address_number', 'address_complement','neighborhood','city','state','phone', 'email','occupation','family_income', 'dependents_count','household_members','status')
    search_fields = ('beneficiary_name','id_beneficiary')




admin.site.register(Beneficiary,BeneficiaryAdmin)

