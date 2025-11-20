from django import forms
from django.core.exceptions import ValidationError
from stock.models import Supplier, StockEntry, Stock

class suppliers_form(forms.ModelForm):
    
    class Meta:
        model = Supplier
        fields = ("supplier_name","supplier_type","tax_id","zip_code","street","address_number","address_complement","neighborhood","city","state","phone","email","is_anonymous")
        widgets = {
                'supplier_name': forms.TextInput(attrs={
                    'class': 'block w-full rounded-lg border-gray-300 bg-primary border border-border-light placeholder-gray-400 '
                            'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2'
                }),
                'supplier_type':forms.Select(attrs={
                    'class': 'block w-full rounded-lg border-gray-300 bg-primary border border-border-light '
                            'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2'
                }),
                'tax_id': forms.TextInput(attrs={
                    'class': 'block w-full rounded-lg border-gray-300 bg-primary border border-border-light placeholder-gray-400 '
                            'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2'
                }),
                'zip_code': forms.TextInput(attrs={
                    'class': 'block w-full rounded-lg border-gray-300 bg-primary border border-border-light placeholder-gray-400 '
                            'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2'
                }),
                'street': forms.TextInput(attrs={
                    'class': 'block w-full rounded-lg border-gray-300 bg-primary border border-border-light placeholder-gray-400 '
                            'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2'
                }),
                'address_number': forms.NumberInput(attrs={
                    'class': 'block w-full rounded-lg border-gray-300 bg-primary border border-border-light placeholder-gray-400 '
                            'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2'
                }),
                'address_complement': forms.TextInput(attrs={
                    'class': 'block w-full rounded-lg border-gray-300 bg-primary border border-border-light placeholder-gray-400 '
                            'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2'
                }),
                'neighborhood': forms.TextInput(attrs={
                    'class': 'block w-full rounded-lg border-gray-300 bg-primary border border-border-light placeholder-gray-400 '
                            'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2'
                }),
                'city': forms.TextInput(attrs={
                    'class': 'block w-full rounded-lg border-gray-300 bg-primary border border-border-light placeholder-gray-400 '
                            'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2'
                }),
                'state': forms.Select(attrs={
                    'class': 'block w-full rounded-lg border-gray-300 bg-primary border border-border-light '
                            'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2'
                }),
                'phone': forms.TextInput(attrs={
                    'class': 'block w-full rounded-lg border-gray-300 bg-primary border border-border-light placeholder-gray-400 '
                            'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2'
                }),
                'email': forms.EmailInput(attrs={
                    'class': 'block w-full rounded-lg border-gray-300 bg-primary border border-border-light placeholder-gray-400 '
                            'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2'
                }),
                'is_anonymous': forms.CheckboxInput(attrs={
                    'class': 'h-5 w-5 text-blue-600 border-gray-300 rounded focus:ring-blue-500'
                }),
            }





class StockEntryForm(forms.ModelForm):
    quantity = forms.IntegerField(
        min_value=1,
        initial=1,
        label='Quantidade de Entradas',
        widget=forms.NumberInput(attrs={
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent',
            'placeholder': 'Quantidade de cestas básicas',
        }),
        help_text='Número de cestas básicas a serem registradas'
    )
    
    class Meta:
        model = StockEntry
        fields = ['supplier_fk']
        
        widgets = {
            'supplier_fk': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent',
            }),
        }
        
        labels = {
            'supplier_fk': 'Fornecedor',
        }

    def __init__(self, *args, **kwargs):
        self.stock = kwargs.pop('stock', None)  
        super(StockEntryForm, self).__init__(*args, **kwargs)
        self.fields['supplier_fk'].required = True
        self.fields['supplier_fk'].queryset = Supplier.objects.all()
        
    def save(self, commit=True):
        
        return None