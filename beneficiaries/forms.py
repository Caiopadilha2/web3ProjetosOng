from django import forms
from django.core.exceptions import ValidationError
import re
from beneficiaries.models import Beneficiary 
from projects.models import Project

class BeneficiariesModelForm(forms.ModelForm):
     #  NÃO APAGAR FIX PARA: BRUNO 
    # projeto = forms.ModelChoiceField(
    #     queryset = Project.objects.all(),
    #     required = True,
    #     label= 'Projeto',
    #     widget= forms.Select(attrs = {"class" : "block w-full rounded-lg border border-border-light bg-primary border focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2"
    #     })

    # )




    class Meta:
        model = Beneficiary
        fields = ("beneficiary_name","birth_date","cpf","zip_code","street","address_number","address_complement","neighborhood","city","state","phone","email","occupation","family_income","dependents_count","household_members","status","projects",)
        #  NÃO APAGAR FIX PARA: BRUNO                     
        # fields = ("beneficiary_name","birth_date","cpf","zip_code","street","address_number","address_complement","neighborhood","city","state","phone","email","occupation","family_income","dependents_count","household_members","status","projeto")



        widgets = {
            'beneficiary_name': forms.TextInput(attrs={
                'class': 'mt-1 placeholder-subtitle block w-full rounded-lg border border-border-light bg-primary border placeholder-gray-400 '
                         'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2 shadow-sm',
                'placeholder': 'Digite o nome completo',
            }),
            'birth_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'mt-1 placeholder-subtitle block w-full rounded-lg border border-border-light bg-primary border placeholder-gray-400 '
                         'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2 shadow-sm',
            }),
            'cpf': forms.TextInput(attrs={
                'class': 'mt-1 placeholder-subtitle block w-full rounded-lg border border-border-light bg-primary border placeholder-gray-400 '
                         'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2 shadow-sm',
                'placeholder': '000.000.000-00'           }),
            'zip_code': forms.TextInput(attrs={
                'class': 'mt-1 placeholder-subtitle block w-full rounded-lg border border-border-light bg-primary border placeholder-gray-400 '
                         'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2 shadow-sm',
                'placeholder': '00.000-00'
            }),
            'street': forms.TextInput(attrs={
                'class': 'mt-1 placeholder-subtitle block w-full rounded-lg border border-border-light bg-primary border placeholder-gray-400 '
                         'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2 shadow-sm',
                'placeholder': 'Digite o endereço aqui'
            }),
            'address_number': forms.NumberInput(attrs={
                'class': 'mt-1 placeholder-subtitle block w-full rounded-lg border border-border-light bg-primary border placeholder-gray-400 '
                         'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2 shadow-sm',
                'placeholder': 'Nº: casa',        
            }),
            'address_complement': forms.TextInput(attrs={
                'class': 'mt-1 placeholder-subtitle block w-full rounded-lg border border-border-light bg-primary border placeholder-gray-400 '
                         'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2 shadow-sm',
            }),
            'neighborhood': forms.TextInput(attrs={
                'class': 'mt-1 placeholder-subtitle block w-full rounded-lg border border-border-light bg-primary border placeholder-gray-400 '
                         'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2 shadow-sm',
                'placeholder': 'Digite o bairro',
            }),
            'city': forms.TextInput(attrs={
                'class': 'mt-1 placeholder-subtitle block w-full rounded-lg border border-border-light bg-primary border placeholder-gray-400 '
                         'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2 shadow-sm',
                'placeholder': 'Digite a cidade',         
            }),
            'state': forms.Select(attrs={
                'class': 'mt-1 placeholder-subtitle block w-full rounded-lg border border-border-light bg-primary border '
                         'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2 shadow-sm'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'mt-1 placeholder-subtitle block w-full rounded-lg border border-border-light bg-primary border placeholder-gray-400 '
                         'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2 shadow-sm',
                'placeholder' : '(00) 00000-0000',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'mt-1 placeholder-subtitle block w-full rounded-lg border border-border-light bg-primary border placeholder-gray-400 '
                         'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2 shadow-sm',
                'placeholder' : 'Digite o email'

            }),
            'dependents_count': forms.NumberInput(attrs={
                'class': 'mt-1 placeholder-subtitle block w-full rounded-lg border border-border-light bg-primary border placeholder-gray-400 '
                         'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2 shadow-sm',
                'placeholder': '01'         
            }),
            'household_members': forms.NumberInput(attrs={
                'class': 'mt-1 placeholder-subtitle block w-full rounded-lg border border-border-light bg-primary border placeholder-gray-400 '
                         'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2 shadow-sm',
                'placeholder': '01'
            }),
            'status': forms.Select(attrs={
                'class': 'mt-1 placeholder-subtitle block w-full rounded-lg border border-border-light bg-primary border '
                         'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2 shadow-sm',
                'placeholder': 'UF'
            }),
            'occupation': forms.TextInput(attrs={
                'class': 'mt-1 placeholder-subtitle block w-full rounded-lg border border-border-light bg-primary border placeholder-gray-400 '
                         'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2 shadow-sm',
             'placeholder' : 'Digite a Profissâo',

            }),
            'family_income': forms.NumberInput(attrs={
                'class': 'mt-1 placeholder-subtitle block w-full rounded-lg border border-border-light bg-primary border placeholder-gray-400 '
                         'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2 shadow-sm',
                'placeholder': 'R$: 000,00'         
            }),
            'projects': forms.SelectMultiple(attrs={
                'class': 'block w-full rounded-lg border-gray-300 bg-white '
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
    projeto = forms.ModelChoiceField(
        queryset = Project.objects.all(),
        required = True,
        label= 'Projeto',
        widget= forms.Select(attrs = {"class" : "block w-full rounded-lg border border-border-light bg-primary border focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2"
        })

    )
    
    class Meta:
        model = Beneficiary
        fields = ("beneficiary_name","birth_date","cpf","zip_code","street","address_number","address_complement","neighborhood","city","state","phone","email","occupation","family_income","dependents_count","household_members",)
        widgets = {
            'beneficiary_name': forms.TextInput(attrs={
                'class': 'mt-1 placeholder-black block w-full rounded-lg border border-border-light bg-primary placeholder-gray-400 focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2 shadow-sm',
                'placeholder': 'Digite seu nome completo',
         
            }),
            'birth_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'mt-1 placeholder-subtitle block w-full rounded-lg border border-border-light bg-primary placeholder-gray-400 '
                         'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2 shadow-sm',
                

            }),
            'cpf': forms.TextInput(attrs={
                'class': 'mt-1 placeholder-subtitle block w-full rounded-lg border border-border-light bg-primary placeholder-gray-400 '
                         'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2 shadow-sm',
                'placeholder' : '000.000.000-00'

            }),
            'zip_code': forms.TextInput(attrs={
                'class': 'mt-1 placeholder-subtitle block w-full rounded-lg border border-border-light bg-primary placeholder-gray-400 '
                         'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2 shadow-sm',
                'placeholder' : '00.000-00'

            }),
            'street': forms.TextInput(attrs={
                'class': 'mt-1 placeholder-subtitle block w-full rounded-lg border border-border-light bg-primary placeholder-gray-400 '
                         'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2 shadow-sm',
                'placeholder' : 'Digite seu Logradouro'

            }),
            'address_number': forms.NumberInput(attrs={
                'class': 'mt-1 placeholder-subtitle block w-full rounded-lg border border-border-light bg-primary placeholder-gray-400 '
                         'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2 shadow-sm',
                'placeholder' : 'Nº da Casa'

            }),
            'address_complement': forms.TextInput(attrs={
                'class': 'mt-1 placeholder-subtitle block w-full rounded-lg border border-border-light bg-primary placeholder-gray-400 '
                         'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2 shadow-sm',
                'placeholder' : 'Bloco 2, Ap 345...Quadra 1 lote 8'

            }),
            'neighborhood': forms.TextInput(attrs={
                'class': 'mt-1 placeholder-subtitle block w-full rounded-lg border border-border-light bg-primary placeholder-gray-400 '
                         'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2 shadow-sm',
                'placeholder' : 'Digite seu bairro'

            }),
            'city': forms.TextInput(attrs={
                'class': 'mt-1 placeholder-subtitle block w-full rounded-lg border border-border-light bg-primary placeholder-gray-400 '
                         'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2 shadow-sm',
                'placeholder' : 'Digite seu município'

            }),
            'state': forms.Select(attrs={
                'class': 'mt-1 placeholder-subtitle block w-full rounded-lg border border-border-light bg-primary '
                         'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2 shadow-sm',
                'placeholder' : 'UF'

            }),
            'phone': forms.TextInput(attrs={
                'class': 'mt-1 placeholder-subtitle block w-full rounded-lg border border-border-light bg-primary placeholder-gray-400 '
                         'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2 shadow-sm',
                'placeholder' : '(00) 00000-0000'

            }),
            'email': forms.EmailInput(attrs={
                'class': 'mt-1 placeholder-subtitle block w-full rounded-lg border border-border-light bg-primary placeholder-gray-400 '
                         'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2 shadow-sm',
                'placeholder' : 'example@examples.com.br'

            }),
            'dependents_count': forms.NumberInput(attrs={
                'class': 'mt-1 placeholder-black block w-full rounded-lg border border-border-light bg-primary placeholder-gray-400 focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2 shadow-sm',
                'placeholder' : '01'              
            }),
            'household_members': forms.NumberInput(attrs={
                'class': 'mt-1 placeholder-subtitle block w-full rounded-lg border border-border-light bg-primary placeholder-gray-400 '
                         'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2 shadow-sm',
                'placeholder' : '01'

            }),
            'occupation': forms.TextInput(attrs={
                'class': 'mt-1 placeholder-subtitle block w-full rounded-lg border border-border-light bg-primary placeholder-gray-400 '
                         'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2 shadow-sm',
                'placeholder' : 'Digite sua profissão'

            }),
            'family_income': forms.NumberInput(attrs={
                'class': 'mt-1 placeholder-subtitle block w-full rounded-lg border border-border-light bg-primary placeholder-gray-400 '
                         'focus:border-blue-500 focus:ring focus:ring-blue-200 text-gray-700 p-2 shadow-sm',
                

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

    def clean_project_income(self):
        project = self.cleaned_data.get('project')

        if project == '':
            raise ValidationError("Escolha um Projeto")
        return project      
