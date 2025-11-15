from django.contrib import admin
from donations.models import Donation

# Register your models here.

class DonationAdmin(admin.ModelAdmin):

    list_display = ('id_donation','beneficiary_fk','stock_entry_fk','description','donation_date','donation_time','donation_month','donation_year')

    search_fields = ('id_donation','beneficiary_fk')


admin.site.register(Donation,DonationAdmin)