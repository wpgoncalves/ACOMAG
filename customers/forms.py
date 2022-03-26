from django import forms

from customers.models import Adresses, Customers, Emails, Phones


class AdressesForm(forms.ModelForm):

    class Meta:
        model = Adresses
        fields = '__all__'


class PhonesForm(forms.ModelForm):

    class Meta:
        model = Phones
        fields = '__all__'


class EmailsForm(forms.ModelForm):

    class Meta:
        model = Emails
        fields = '__all__'


class CustomersForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CustomersForm, self).__init__(*args, **kwargs)
        self.fields['cpf_cnpj'].widget.attrs['class'] += ' vMaskCpfCnpjField'

    class Meta:
        model = Customers
        fields = '__all__'
