from django import forms
from django.core.exceptions import ValidationError

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):

    validation_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        fields = '__all__'
        exclude = ('change_date', 'create_date')

    def clean_product_name(self):
        cleaned_data = self.cleaned_data['product_name']

        if cleaned_data.lower() in self.validation_list:
            raise ValidationError('Такое название использовать запрещено.')
        return cleaned_data

    def clean_product_description(self):
        cleaned_data = self.cleaned_data['product_description']

        if cleaned_data in self.validation_list:
            raise ValidationError('Такое описание использовать запрещено.')
        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'
