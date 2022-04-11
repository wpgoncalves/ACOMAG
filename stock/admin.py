from django.contrib import admin

from stock.forms import HoldersForm, ItemForm, StockForm
from stock.models import Holders, Items, Stock


class StockInline(admin.TabularInline):
    model = Stock
    extra = 1
    verbose_name = 'Estoque'
    verbose_name_plural = 'Estoques'


@admin.register(Items)
class ItemsAdmin(admin.ModelAdmin):
    form = ItemForm
    inlines = [StockInline]
    list_display = ('code', 'description', 'supply_branch', 'group', 'value',
                    'to_supply', 'discontinued')
    search_fields = ('code', 'description')
    list_filter = ('supply_branch', 'group', 'discontinued', 'unit')
    fieldsets = (
        (None, {
            'fields': ('code', 'description', ('supply_branch', 'group'),
                       ('value', 'to_supply'), ('unit', 'quantity_unit',
                       'min_quantity_supply'), 'discontinued'),
            'description':
            '<h4><b>*Os campos em negrito são obrigatórios.</b></h4>',
        }),
    )

    class Media:
        js = ('js/jquery.mask.min.js', 'stock/js/script.js')


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    form = StockForm
    list_display = ('item', 'amount', 'holder', 'updated')
    search_fields = ('item', )
    list_filter = ('holder', )
    fieldsets = (
        (None, {
            'fields': ('item', ('amount', 'holder')),
            'description':
            '<h4><b>*Os campos em negrito são obrigatórios.</b></h4>',
        }),
    )


@admin.register(Holders)
class HoldersAdmin(admin.ModelAdmin):
    form = HoldersForm
    list_display = ('description', 'operator', 'registration', 'discontinued')
    search_fields = ('description', 'operator', 'registration')
    list_filter = ('discontinued', )
    fieldsets = (
        (None, {
            'fields': ('description', 'operator', 'registration', 'comments',
                       'discontinued'),
            'description':
            '<h4><b>*Os campos em negrito são obrigatórios.</b></h4>',
        }),
    )

    class Media:
        js = ('js/jquery.mask.min.js', 'stock/js/script.js')
