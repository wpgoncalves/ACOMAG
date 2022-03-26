from django import forms

from customers.models import Adresses, Customers, Emails, Phones


class AdressesForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AdressesForm, self).__init__(*args, **kwargs)
        self.fields['cep'].widget.attrs['class'] += ' vMaskCepField'

    class Meta:
        model = Adresses
        fields = '__all__'


class PhonesForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PhonesForm, self).__init__(*args, **kwargs)
        self.fields['number'].widget.attrs['class'] += ' vMaskPhoneField'

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
        # self.fields['name'].widget.attrs['style'] = 'text-transform: capitalize;'

    class Meta:
        model = Customers
        fields = '__all__'
        # widgets = {
        #     'name': forms.TextInput(attrs={
        #         'style': 'text-transform: capitalize;'
        #     })
        # }
