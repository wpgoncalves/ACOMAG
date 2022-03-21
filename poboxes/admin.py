from django.contrib import admin

from poboxes.models import (Adresses, Customers, Emails, Phones, POBoxes,
                            Rentals)


@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
    list_display = ('name', 'cpf_cnpj', 'kind')
    search_fields = ('cpf_cnpj', 'name')
    list_filter = ('kind',)


@admin.register(Adresses)
class AdressesAdmin(admin.ModelAdmin):
    list_display = ('cep', 'type', 'address', 'district', 'city', 'state')
    search_fields = ('cep', 'address')
    list_filter = ('type', 'city', 'district', 'state')


@admin.register(Phones)
class PhonesAdmin(admin.ModelAdmin):
    list_display = ('number', 'type')
    search_fields = ('number',)
    list_filter = ('type',)


@admin.register(Emails)
class EmailsAdmin(admin.ModelAdmin):
    list_display = ('email',)
    search_fields = ('email',)


@admin.register(POBoxes)
class POBoxesAdmin(admin.ModelAdmin):
    list_display = ('number', 'type', 'extra_key', 'active')
    search_fields = ('number',)
    list_filter = ('type', 'extra_key', 'pib', 'active')


@admin.register(Rentals)
class RentalsAdmin(admin.ModelAdmin):
    list_display = ('pobox_id', 'customer_id', 'start_validity',
                    'end_validity', 'rent_value', 'warned_in',
                    'sealed_in', 'expired')
    search_fields = ('pobox_id', '')
    list_filter = ('pobox_id', 'customer_id', 'expired')
