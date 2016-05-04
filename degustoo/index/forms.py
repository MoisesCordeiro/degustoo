from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext as _

from degAuth.models import Usuario
from restaurante.models import GerenciadorRestaurante, Restaurante
from core.plugins.cnpj import Cnpj

class Form_Registro(ModelForm):

    nome = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    sobrenome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    telefone = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    senha1 = forms.CharField(min_length=6, max_length=12, widget=forms.PasswordInput(attrs={"class":"form-control"}), label=_("Password"))
    senha2 = forms.CharField(min_length=6, max_length=12, widget=forms.PasswordInput(attrs={"class":"form-control"}), label=_("Password confirmation"))

    class Meta:
        model = Usuario
        fields = ['email', 'telefone']
    
    def clean_senha2(self):
        pass1 = self.cleaned_data['senha1']
        pass2 = self.cleaned_data['senha2']
        
        if (pass1 and pass2) and (pass1 == pass2):
            return pass2
        else:
            raise forms.ValidationError(_("Password fields do not match"))

class Form_Restaurant_Register(forms.Form):
    CHOICES = (
        (0, "Comum"),
        (1, "Diamante"),
    )

    DO_DELIVERY = (
        (True, 'Sim'),
        (False, 'Não'),
    )

    # Dados do responsável pelo restaurante
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'E-mail do estabelecimento'}))
    telefone = forms.RegexField(regex=r"^\d{8,20}$", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Telefone do estabelecimento'}))
    nome = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nome do estabelecimento'}))
    cnpj = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'CNPJ'}))
    #password_a = forms.CharField(min_length=6, label=_("Password"), max_length=16, widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':_('Password')}))
    #password_b = forms.CharField(min_length=6, label=_("Password confirmation"), max_length=16, widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':_('Password confirmation')}))
    
    tipo_cozinha = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    faz_delivery = forms.ChoiceField(choices=DO_DELIVERY,widget=forms.Select(attrs={'class':'form-control'}))

    nome_completo_responsavel = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nome completo do responsável'}))
    email_responsavel = forms.CharField(max_length=30, widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'E-mail do responsável'}))
    telefone_responsavel = forms.RegexField(regex=r"^\d{8,20}$", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Telefone do responsável'}))
    
    estado = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Estado'}))
    municipio = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Municipio'}))
    bairro = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Bairro'}))
    rua = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Rua'}))
    numero = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Número'}))
    complemento = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Complemento'}), required=False)
    cep = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'CEP'}))


    def clean_email(self):
        email = self.cleaned_data['email']

        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError('Email já registrado. Tente outro endereço.')
        return email

    def clean_telefone(self):
        telefone = self.cleaned_data['telefone']

        if Usuario.objects.filter(telefone=telefone).exists():
            raise forms.ValidationError('Número de telefone já cadastrado. Tente outro número.')
        return telefone

    def clean_cnpj(self):
        cnpj = self.cleaned_data['cnpj']

        if Restaurante.objects.filter(cnpj=cnpj).exists():
            raise forms.ValidationError('Número de cnpj em uso.')
        validator = Cnpj()
        if not validator.validate(cnpj):
            raise forms.ValidationError('Número de cnpj inválido.')
        return cnpj

    def clean_password_b(self):
        password1 = self.cleaned_data['password_a']
        password2 = self.cleaned_data['password_b']

        if (password1 and password2) and (password1 == password2):
            return password2
        else:
            raise forms.ValidationError("Passwords do not match")

    def clean_email_responsavel(self):
        email = self.cleaned_data['email_responsavel']
        if not GerenciadorRestaurante.objects.filter(email=email).exists():
            return email
        raise forms.ValidationError(_("Email already in use"))


    def clean_telefone_responsavel(self):
        telefone = self.cleaned_data['telefone_responsavel']
        if not GerenciadorRestaurante.objects.filter(telefone=telefone):
            return telefone
        raise forms.ValidationError(_("Phone number already in use"))

class Form_Login(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()