from django.contrib import admin

from poboxes.models import POBoxes, Rentals


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
