from django import forms
from django.core.exceptions import ValidationError
import re
from beneficiaries.models import Beneficiary 

class BeneficiariesModelForm(forms.ModelForm):
    class Meta:
        model = Beneficiary
        fields = ("beneficiary_name","birth_date","cpf","zip_code","street","address_number","address_complement","neighborhood","city","state","phone","email","occupation","family_income","dependents_count","household_members","status",)
        widgets = {
            'beneficiary_name': forms.TextInput(attrs={
                'class': 'block w-full rounded-lg border-gray-300 bg-white placeholder-gray-400 '
                         'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2'
            }),
            'birth_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'block w-full rounded-lg border-gray-300 bg-white placeholder-gray-400 '
                         'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2'
            }),
            'cpf': forms.TextInput(attrs={
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
            'dependents_count': forms.NumberInput(attrs={
                'class': 'block w-full rounded-lg border-gray-300 bg-white placeholder-gray-400 '
                         'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2'
            }),
            'household_members': forms.NumberInput(attrs={
                'class': 'block w-full rounded-lg border-gray-300 bg-white placeholder-gray-400 '
                         'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2'
            }),
            'status': forms.Select(attrs={
                'class': 'block w-full rounded-lg border-gray-300 bg-white '
                         'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2'
            }),
            'occupation': forms.TextInput(attrs={
                'class': 'block w-full rounded-lg border-gray-300 bg-white placeholder-gray-400 '
                         'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2'
            }),
            'family_income': forms.NumberInput(attrs={
                'class': 'block w-full rounded-lg border-gray-300 bg-white placeholder-gray-400 '
                         'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2'
            }),
        }
           
    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')

        if not cpf:
            raise ValidationError("Informe um CPF.")

        cpf = re.sub(r'[^0-9]', '', cpf)

        if len(cpf) != 11 or cpf == cpf[0] * 11:
            raise ValidationError("CPF inválido.")

        soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
        dig1 = ((soma * 10) % 11) % 10
        soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
        dig2 = ((soma * 10) % 11) % 10

        if dig1 != int(cpf[9]) or dig2 != int(cpf[10]):
            raise ValidationError("CPF inválido.")

        return cpf 
    

    def clean_address_number(self):
        address_number = self.cleaned_data.get('address_number')

        if address_number < 0:
            raise ValidationError("Informe um número de endereço válido.")
        return address_number

    def clean_dependents_count(self):
        dependents_count = self.cleaned_data.get('dependents_count')

        if dependents_count < 0:
            raise ValidationError("Informe um número de dependentes válido.")
        return dependents_count

    def clean_household_members(self):
        household_members = self.cleaned_data.get('household_members')

        if household_members < 0:
            raise ValidationError("Informe um número de pessoas que moram na mesma residência.")
        return household_members 

    def clean_family_income(self):
        family_income = self.cleaned_data.get('family_income')

        if family_income < 0:
            raise ValidationError("Informe uma renda familiar válida.")
        return family_income       
    

class auto_register_Form(forms.ModelForm):
    
    class Meta:
        model = Beneficiary
        fields = ("beneficiary_name","birth_date","cpf","zip_code","street","address_number","address_complement","neighborhood","city","state","phone","email","occupation","family_income","dependents_count","household_members",)
        widgets = {
            'beneficiary_name': forms.TextInput(attrs={
                'class': 'block w-full rounded-lg border-gray-300 bg-white placeholder-gray-400 '
                         'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2'
            }),
            'birth_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'block w-full rounded-lg border-gray-300 bg-white placeholder-gray-400 '
                         'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2'
            }),
            'cpf': forms.TextInput(attrs={
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
            'dependents_count': forms.NumberInput(attrs={
                'class': 'block w-full rounded-lg border-gray-300 bg-white placeholder-gray-400 '
                         'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2'
            }),
            'household_members': forms.NumberInput(attrs={
                'class': 'block w-full rounded-lg border-gray-300 bg-white placeholder-gray-400 '
                         'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2'
            }),
            'occupation': forms.TextInput(attrs={
                'class': 'block w-full rounded-lg border-gray-300 bg-white placeholder-gray-400 '
                         'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2'
            }),
            'family_income': forms.NumberInput(attrs={
                'class': 'block w-full rounded-lg border-gray-300 bg-white placeholder-gray-400 '
                         'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2'
            }),
        }
        
        def clean_cpf(self):
            cpf = self.cleaned_data.get('cpf')

            if not cpf:
                raise ValidationError("Informe um CPF.")

            cpf = re.sub(r'[^0-9]', '', cpf)

            if len(cpf) != 11 or cpf == cpf[0] * 11:
                raise ValidationError("CPF inválido.")

            soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
            dig1 = ((soma * 10) % 11) % 10
            soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
            dig2 = ((soma * 10) % 11) % 10

            if dig1 != int(cpf[9]) or dig2 != int(cpf[10]):
                raise ValidationError("CPF inválido.")

            return cpf 
    

    def clean_address_number(self):
        address_number = self.cleaned_data.get('address_number')

        if address_number < 0:
            raise ValidationError("Informe um número de endereço válido.")
        return address_number

    def clean_dependents_count(self):
        dependents_count = self.cleaned_data.get('dependents_count')

        if dependents_count < 0:
            raise ValidationError("Informe um número de dependentes válido.")
        return dependents_count

    def clean_household_members(self):
        household_members = self.cleaned_data.get('household_members')

        if household_members < 0:
            raise ValidationError("Informe um número de pessoas que moram na mesma residência.")
        return household_members 

    def clean_family_income(self):
        family_income = self.cleaned_data.get('family_income')

        if family_income < 0:
            raise ValidationError("Informe uma renda familiar válida.")
        return family_income       
