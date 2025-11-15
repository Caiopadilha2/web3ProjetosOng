from django import forms
from django.core.exceptions import ValidationError
from stock.models import Supplier

class suppliers_form(forms.ModelForm):
    
    class Meta:
        model = Supplier
        fields = ("supplier_name","supplier_type","tax_id","zip_code","street","address_number","address_complement","neighborhood","city","state","phone","email","is_anonymous")
        widgets = {
                'supplier_name': forms.TextInput(attrs={
                    'class': 'block w-full rounded-lg border-gray-300 bg-white placeholder-gray-400 '
                            'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2'
                }),
                'supplier_type':forms.Select(attrs={
                    'class': 'block w-full rounded-lg border-gray-300 bg-white '
                            'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2'
                }),
                'tax_id': forms.TextInput(attrs={
                    'class': 'block w-full rounded-lg border-gray-300 bg-white placeholder-gray-400 '
                            'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2'
                }),
                'zip_code': forms.TextInput(attrs={
                    'class': 'block w-full rounded-lg border-gray-300 bg-white placeholder-gray-400 '
                            'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2'
                }),
                'street': forms.TextInput(attrs={
                    'class': 'block w-full rounded-lg border-gray-300 bg-white placeholder-gray-400 '
                            'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2'
                }),
                'address_number': forms.NumberInput(attrs={
                    'class': 'block w-full rounded-lg border-gray-300 bg-white placeholder-gray-400 '
                            'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2'
                }),
                'address_complement': forms.TextInput(attrs={
                    'class': 'block w-full rounded-lg border-gray-300 bg-white placeholder-gray-400 '
                            'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2'
                }),
                'neighborhood': forms.TextInput(attrs={
                    'class': 'block w-full rounded-lg border-gray-300 bg-white placeholder-gray-400 '
                            'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2'
                }),
                'city': forms.TextInput(attrs={
                    'class': 'block w-full rounded-lg border-gray-300 bg-white placeholder-gray-400 '
                            'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2'
                }),
                'state': forms.Select(attrs={
                    'class': 'block w-full rounded-lg border-gray-300 bg-white '
                            'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2'
                }),
                'phone': forms.TextInput(attrs={
                    'class': 'block w-full rounded-lg border-gray-300 bg-white placeholder-gray-400 '
                            'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2'
                }),
                'email': forms.EmailInput(attrs={
                    'class': 'block w-full rounded-lg border-gray-300 bg-white placeholder-gray-400 '
                            'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2'
                }),
                'is_anonymous': forms.CheckboxInput(attrs={
                    'class': 'h-5 w-5 text-blue-600 border-gray-300 rounded focus:ring-blue-500'
                }),
            }
