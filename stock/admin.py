from django.contrib import admin
from stock.models import Supplier, Stock, StockEntry


# Register your models here.
class SupplierAdmin(admin.ModelAdmin):

    list_display = (
        'id_supplier',
        'supplier_name',
        'supplier_type',
        'tax_id',
        'zip_code',
        'street',
        'address_number',
        'address_complement',
        'neighborhood',
        'city',
        'state',
        'phone',
        'email',
        'is_anonymous',
        )
    
    search_fields = ('id_supplier','supplier_name','city')


admin.site.register(Supplier,SupplierAdmin)

class StockAdmin(admin.ModelAdmin):
    list_display = (
        'id_stock',
        'stock_name',
        'stock_description',
        'quantity',
        'update_at'
        )
    
    search_fields = ('id_stock','stock_name')

admin.site.register(Stock,StockAdmin)



class StockEntryAdmin(admin.ModelAdmin):
    list_display = (
        'id_stockentry',
        'stock_fk',
        'supplier_fk',
        'batch',
        'entry_date',
        'entry_time',
        'exit_date',
        'exit_time',
        'is_available',
        )
    
    search_fields = (
        'id_stockentry',
        'stock_fk',
        'supplier_fk',
        'batch',
        'is_available',
        )
    

admin.site.register(StockEntry,StockEntryAdmin)
    