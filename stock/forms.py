from django import forms
from utils.tools import string_capitalize

from stock.models import Holders, Items, Stock


class ItemForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)

        self.fields['code'].widget.attrs['class'] += ' vMaskCodeField'

        self.fields['description'].widget.attrs['style'] = \
            'text-transform: capitalize;'

    def clean_description(self):
        return string_capitalize(self.cleaned_data['description'])

    class Meta:
        model = Items
        fields = '__all__'


class StockForm(forms.ModelForm):

    class Meta:
        model = Stock
        fields = '__all__'


class HoldersForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(HoldersForm, self).__init__(*args, **kwargs)

        self.fields['registration'].widget.attrs['class'] += \
            ' vMaskRegistrationField'

        self.fields['description'].widget.attrs['style'] = \
            'text-transform: capitalize;'

        self.fields['operator'].widget.attrs['style'] = \
            'text-transform: capitalize;'

    def clean_description(self):
        return string_capitalize(self.cleaned_data['description'])

    def clean_operator(self):
        return string_capitalize(self.cleaned_data['operator'])

    class Meta:
        model = Holders
        fields = '__all__'
