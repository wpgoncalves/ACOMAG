from django.contrib import admin
from poboxes.models import Adresses, Customers, POBoxes, Phones, Emails


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
