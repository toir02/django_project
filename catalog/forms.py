from django import forms
from django.core.exceptions import ValidationError

from catalog.models import Product


class ProductForm(forms.ModelForm):

    validation_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        fields = '__all__'
        exclude = ('change_date',)

    def clean_product_name(self):
        cleaned_data = self.cleaned_data['product_name']

        if cleaned_data in self.validation_list:
            raise ValidationError('Такое название использовать запрещено.')
        return cleaned_data
