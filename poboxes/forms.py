from django import forms

from poboxes.models import POBoxes, Rentals


class POBoxesForm(forms.ModelForm):

    class Meta:
        model = POBoxes
        fields = '__all__'


class RentalsForm(forms.ModelForm):

    class Meta:
        model = Rentals
        fields = '__all__'
