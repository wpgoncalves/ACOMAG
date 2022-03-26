from django.contrib import admin

from customers.forms import AdressesForm, CustomersForm, PhonesForm
from customers.models import Adresses, Customers, Emails, Phones


@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
    list_display = ('name', 'cpf_cnpj', 'kind')
    search_fields = ('cpf_cnpj', 'name')
    list_filter = ('kind',)
    form = CustomersForm

    class Media:
        js = ('js/jquery.mask.min.js', 'customers/js/script.js')
        # css = {'all': ('customers/css/style.css',)}


@admin.register(Adresses)
class AdressesAdmin(admin.ModelAdmin):
    list_display = ('cep', 'type', 'address', 'district', 'city', 'state')
    search_fields = ('cep', 'address')
    list_filter = ('type', 'city', 'district', 'state')
    form = AdressesForm

    class Media:
        js = ('js/jquery.mask.min.js', 'customers/js/script.js')


@admin.register(Phones)
class PhonesAdmin(admin.ModelAdmin):
    list_display = ('number', 'type')
    search_fields = ('number',)
    list_filter = ('type',)
    form = PhonesForm

    class Media:
        js = ('js/jquery.mask.min.js', 'customers/js/script.js')


@admin.register(Emails)
class EmailsAdmin(admin.ModelAdmin):
    list_display = ('email',)
    search_fields = ('email',)
